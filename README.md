# 🧠 CloudWalk - Interviewers Bias Analyzer

> Uncover hidden biases and improve your interviewing skills.

This application leverages OpenAI to analyze interview transcripts, helping you detect biases and improve your hiring process with actionable insights and tailored recommendations.

## 🚀 How It Works

1. **Enter your OpenAI API Key**
   - Input your API key in the field provided
   - For CloudWalk team members, request access for the API Key in the **#get-hands-dirty-with-llms** Slack channel

2. **Paste the Interview Transcript**
   - Add the transcript of your interview in the text box

3. **Analyze and Improve**
   - Click **"Analyze Transcript"** to receive:
     - An overall assessment of the interview
     - Identification of potential biases
     - Suggestions for improvements
     - Recommendations for better interview questions

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ingridytakada/interview-analysis-app.git
   cd interview-analysis-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## 🌟 Features

- **Bias Detection**: Spot unconscious biases in interview questions
- **Recommendations**: Improve your interviewing technique with tailored advice
- **CloudWalk Alignment**: Supports CloudWalk's mission for fairness and inclusivity

## 📂 Contents

- `streamlit_app.py` - Main application script
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `.gitignore` - Excluded files from the repository
