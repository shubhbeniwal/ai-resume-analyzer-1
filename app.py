import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_analyzer import analyze_resume

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Resume Analyzer | Shubh Beniwal",
    page_icon="📄",
    layout="wide"
)

# ---------------------------
# HEADER / BRANDING
# ---------------------------
st.title("📄 AI Resume Analyzer")
st.markdown("### 🚀 Built by **Shubh Beniwal**")
st.markdown("AI-powered resume evaluation using LLMs for ATS scoring and skill insights")

st.markdown("---")

# ---------------------------
# SIDEBAR (IDENTITY + PROJECT CONTEXT)
# ---------------------------
st.sidebar.title("👨‍💻 Developer")

st.sidebar.markdown("**Shubh Beniwal**")
st.sidebar.markdown("CSE (AI & Robotics), VIT Chennai")

st.sidebar.markdown("---")

st.sidebar.subheader("📌 What this project does")
st.sidebar.write("""
- Parses PDF resumes  
- Uses AI to analyze content  
- Gives ATS-style feedback  
- Identifies skill gaps  
""")

st.sidebar.markdown("---")

st.sidebar.subheader("🔗 Links")
st.sidebar.write("GitHub: github.com/shubhbeniwal")
st.sidebar.write("LinkedIn: linkedin.com/in/shubh-beniwal")

# ---------------------------
# MAIN UI
# ---------------------------
uploaded_file = st.file_uploader(
    "📎 Upload Your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("📖 Reading Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume Uploaded Successfully!")

    st.markdown("### 👉 Ready for AI Analysis")

    if st.button("🚀 Analyze Resume"):

        with st.spinner("🧠 AI is analyzing your resume..."):
            analysis = analyze_resume(resume_text)

        st.markdown("---")
        st.subheader("📊 AI Analysis Result")

        st.write(analysis)

# ---------------------------
# FOOTER (OWNERSHIP SIGNATURE)
# ---------------------------
st.markdown("---")
st.markdown("💡 Built with Python + AI by **Shubh Beniwal**")