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

st.markdown("""
### AI-Powered Resume Evaluation Platform

Get intelligent feedback on your resume using Large Language Models (LLMs).

#### Features
- ATS-style Resume Review
- Skill Gap Analysis
- Resume Improvement Suggestions
- AI-Powered Resume Insights

👨‍💻 Built by **Shubh Beniwal**
""")

st.divider()

# ---------------------------
# SIDEBAR (IDENTITY + PROJECT CONTEXT)
# ---------------------------
st.sidebar.title("👨‍💻 Developer")

st.sidebar.markdown("""
### Shubh Beniwal

**AI & Robotics Engineer**

VIT Chennai

---

### Project

AI Resume Analyzer

Built to simulate how modern ATS and AI-powered hiring systems evaluate resumes.

---

### Tech Stack

- Python
- Streamlit
- LLMs (Gemini / Groq)
- PDF Processing

---
""")

st.sidebar.subheader("🔗 Connect")

st.sidebar.markdown(
    "[GitHub](https://github.com/shubhbeniwal)"
)

st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/in/shubh-beniwal/)"
)

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