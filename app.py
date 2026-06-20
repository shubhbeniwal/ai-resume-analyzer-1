import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_analyzer import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    st.success("Resume Uploaded Successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing with Gemini AI..."):
            analysis = analyze_resume(resume_text)

        st.subheader("Analysis Result")

        st.write(analysis)