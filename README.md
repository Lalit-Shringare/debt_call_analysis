# debt_call_analysis


# 📞 Debt Collection Call Analysis Tool

A Streamlit application that analyzes JSON transcripts of debt collection calls to:

- ✅ Detect **Profanity**
- 🔒 Detect **Privacy & Compliance Violations**
- 📊 Analyze **Call Quality Metrics** (Overtalk and Silence)

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the repository

```bash
git clone https://github.com/your-username/debt-call-analyzer.git
cd debt-call-analyzer

### 2. 🐍 Create and activate a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. 📦 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. 🔐 Setup OpenAI API key
Create a .env file in the root directory with your OpenAI API key:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-key-here
⚠️ You can get your API key from https://platform.openai.com/account/api-keys

🚀 Running the App
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Then go to http://localhost:8501 in your browser.
