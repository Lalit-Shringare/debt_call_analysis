import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
# Initialize the client using API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_check_profanity(conversation, speaker):
    messages = [
        {
            "role": "system",
            "content": "You are an assistant helping identify profanity in debt collection transcripts."
        },
        {
            "role": "user",
            "content": f"Analyze the following conversation and tell me if the {speaker} used any profane language. Respond with only 'Yes' or 'No'.\n\n{conversation}"
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return "yes" in response.choices[0].message.content.lower()

def llm_check_compliance(conversation):
    messages = [
        {
            "role": "system",
            "content": "You are an assistant helping verify compliance in debt collection transcripts."
        },
        {
            "role": "user",
            "content": "Determine if the agent shared sensitive information like balance or account details before verifying identity (DOB, address, SSN). Respond with only 'Yes' or 'No'.\n\n" + str(conversation)
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return "yes" in response.choices[0].message.content.lower()
