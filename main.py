import streamlit as st
from PyPDF2 import PdfReader
import io
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title= "Gini AI Resume Critiquer", page_icon="⚒️", layout="centered")

st.title("Gini AI Resume Critiquer")
st.markdown("Upload your resume and get an AI-powered response that suits your needs")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume in PDF or TXT format", type=["pdf", "txt"])
job_role = st.text_input("What position or job role do you desire (optional)?")
analyze = st.button("Analyze Resume")


def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")  # utf-8 is the standard file encoding

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general applications'}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""

        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
            You are an expert resume reviewer with years of experience in HR and recruitment.

            Task:
            {prompt}
            """,
            config={
                "temperature": 0.7,
                "max_output_tokens": 500
            }
        )

        st.markdown("### Analysis Results")
        st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
