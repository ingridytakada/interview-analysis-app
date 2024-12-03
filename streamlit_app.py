import streamlit as st
import openai

# Função para analisar a transcrição
def analyze_transcript(transcript, api_key):
    """
    Envia a transcrição para a API OpenAI e retorna a análise da entrevista.
    """
    openai.api_key = api_key

    # Configuração das mensagens
    messages = [
        {"role": "system", "content": "You are an expert in interview techniques and bias detection."},
        {
            "role": "user",
            "content": f"""
            Your task is to analyze the transcript of a job interview, evaluate the interviewer's performance, identify any biased questions, and suggest improvements.

            Transcript: {transcript}

            Provide your analysis in the following format:
                a. Overall Assessment:
                    [Provide an overview of the interviewer's performance.]

                b. Biased Questions:
                    [List any biased questions identified, explaining why they are problematic.]

                c. Areas for Improvement:
                    [Suggest specific ways the interviewer can enhance their technique.]

                d. Recommended Questions:
                    [Propose 3-5 alternative or additional questions that would improve the interview.]
            """
        }
    ]

    try:
        # Chamada à API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Failed to call OpenAI API: {e}")

# Interface do Streamlit
st.title("🧠 CloudWalk - Interview Bias Analysis")
st.write(
    "This application analyzes interview transcripts, detects potential biases, and suggests improvements for interviewers. "
    "Enter your interview transcript below to start."
)

# Configuração da chave API
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Entrada para a transcrição
transcript = st.text_area("Insert your interview transcript below:")

# Botão para análise
if st.button("Analyze Transcript"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key.")
    elif not transcript.strip():
        st.error("Please provide a valid transcript.")
    else:
        with st.spinner("Analyzing the transcript..."):
            try:
                # Chama a análise
                analysis = analyze_transcript(transcript, openai_api_key)
                st.subheader("Analysis Result")
                st.write(analysis)
            except Exception as e:
                st.error(f"Error analyzing the transcript: {e}")
