import streamlit as st
from utils.file_loader import load_json
from utils.profanity_detector import detect_profanity, load_bad_words
from utils.compliance_checker import detect_violation
from utils.call_metrics import compute_metrics
from utils.llm_utils import llm_check_profanity, llm_check_compliance
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("Debt Call Analysis")

uploaded_file = st.file_uploader("Upload a JSON call transcript", type="json")
approach = st.selectbox("Choose Analysis Approach", ["Pattern Matching", "LLM"])
task = st.selectbox("Select Analysis Type", ["Profanity Detection", "Compliance Violation", "Call Quality Metrics"])

# Calculate overtalk and silence percentages
def calculate_call_metrics(conversation):
    overtalk = 0
    silence = 0
    total_time = conversation[-1]['etime'] - conversation[0]['stime']

    # Check each pair of adjacent utterances for overtalk and silence
    for i in range(1, len(conversation)):
        current = conversation[i]
        previous = conversation[i - 1]

        # Calculate overlap (overtalk) between two adjacent utterances
        if current['stime'] < previous['etime']:
            overtalk += min(previous['etime'], current['etime']) - current['stime']
        
        # Calculate silence between two adjacent utterances
        silence += max(0, current['stime'] - previous['etime'])

    overtalk_percentage = (overtalk / total_time) * 100
    silence_percentage = (silence / total_time) * 100

    return overtalk_percentage, silence_percentage

# Visualize overtalk and silence metrics
def plot_call_metrics(overtalk_percentage, silence_percentage):
    metrics = ['Overtalk', 'Silence']
    percentages = [overtalk_percentage, silence_percentage]

    # Create the plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=metrics, y=percentages, palette="Blues_d")
    plt.title("Call Quality Metrics (Overtalk & Silence Percentages)")
    plt.xlabel("Metric")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    st.pyplot(plt)


if uploaded_file:
    conversation = load_json(uploaded_file)
    
    if task == "Profanity Detection":
        speaker = st.radio("Check for which speaker?", ['agent', 'borrower'])
        if approach == "Pattern Matching":
            bad_words = load_bad_words()
            found, flagged = detect_profanity(conversation, speaker, bad_words)
            st.success("✅ Profanity Found") if found else st.info("❌ No Profanity Detected")
            if flagged:
                st.write(flagged)
        elif approach == "LLM":
            found = llm_check_profanity(conversation, speaker)
            st.success("✅ Profanity Found (LLM)") if found else st.info("❌ No Profanity Detected (LLM)")


    elif task == "Compliance Violation":
        if approach == "Pattern Matching":
            result = detect_violation(conversation)
            st.success("⚠️ Compliance Violation Detected") if result else st.info("✅ No Violation Found")
        elif approach == "LLM":
            result = llm_check_compliance(conversation)
            st.success("⚠️ Compliance Violation Detected (LLM)") if result else st.info("✅ No Violation Found (LLM)")


    elif task == "Call Quality Metrics":
        overtalk_percentage, silence_percentage = calculate_call_metrics(conversation)
        st.metric("Overtalk %", f"{overtalk_percentage:.2f}%")
        st.metric("Silence %", f"{silence_percentage:.2f}%")

        # Display visualization for call quality metrics
        plot_call_metrics(overtalk_percentage, silence_percentage)
