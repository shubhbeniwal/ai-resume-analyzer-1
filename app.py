import streamlit as st
import re

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_analyzer import analyze_resume
from utils.pdf_generator import generate_pdf_report

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Resume & Job Match Analyzer | Shubh Beniwal",
    page_icon="📄",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------
st.title("📄 AI Resume & Job Match Analyzer")

st.markdown("""
### AI-Powered Resume Evaluation Platform

Get intelligent feedback on your resume using Large Language Models (LLMs).

#### Features
- ATS Match Score
- Resume Analysis
- Job Description Matching
- Skill Gap Analysis
- Resume Improvement Suggestions

👨‍💻 Built by **Shubh Beniwal**
""")

st.divider()

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("👨‍💻 Developer")

st.sidebar.markdown("""
### Shubh Beniwal

**AI & ML Engineer**

VIT Chennai Graduate | Passionate about AI, LLMs, NLP, and Software Engineering

---

### Project

AI Resume & Job Match Analyzer

Built to simulate how modern ATS and AI-powered hiring systems evaluate resumes against job descriptions.

---

### Tech Stack

- Python
- Streamlit
- Groq LLM
- ReportLab
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
# INPUTS
# ---------------------------
uploaded_file = st.file_uploader(
    "📎 Upload Your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description (Optional)",
    height=200,
    placeholder="""
Paste the job description here...

Example:
We are looking for a Python Developer with experience in:
- Python
- SQL
- Machine Learning
- AWS
- Docker
"""
)

# ---------------------------
# ANALYSIS
# ---------------------------
if uploaded_file:

    with st.spinner("📖 Reading Resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume Uploaded Successfully!")

    st.markdown("### 👉 Ready for AI Analysis")

    if st.button("🚀 Analyze Resume"):

        with st.spinner("🧠 AI is analyzing your resume..."):
            analysis = analyze_resume(
                resume_text,
                job_description
            )

        st.markdown("---")
        st.subheader("📊 AI Analysis Result")

        # ---------------------------
        # ATS MATCH SCORE
        # ---------------------------
        score_match = re.search(
            r"ATS Match Score:\s*(\d+)",
            analysis,
            re.IGNORECASE
        )

        if score_match:

            ats_score = int(score_match.group(1))

            st.metric(
                label="ATS Match Score",
                value=f"{ats_score}%"
            )

            st.progress(ats_score / 100)

            if ats_score >= 80:
                st.success("🔥 Strong Match")
            elif ats_score >= 60:
                st.warning("⚡ Moderate Match")
            else:
                st.error("❗ Low Match")

        # ---------------------------
        # MISSING SKILLS
        # ---------------------------
        missing_skills_match = re.search(
            r"## Missing Skills(.*?)(##|$)",
            analysis,
            re.DOTALL | re.IGNORECASE
        )

        missing_skills = []

        if missing_skills_match:

            skills_text = missing_skills_match.group(1)

            for line in skills_text.split("\n"):

                line = line.strip()

                if line.startswith("-"):
                    missing_skills.append(
                        line.replace("-", "").strip()
                    )

        if missing_skills:

            st.markdown("### ⚠️ Missing Skills Detected")

            cols = st.columns(
                min(3, len(missing_skills))
            )

            for i, skill in enumerate(missing_skills):
                cols[i % len(cols)].warning(skill)

        # ---------------------------
        # FULL ANALYSIS
        # ---------------------------
        st.markdown("### 📄 Full Analysis")

        sections = analysis.split("\n\n")

        for section in sections:

            if section.strip():
                st.markdown(section)

        # ---------------------------
        # PDF DOWNLOAD
        # ---------------------------
        pdf_path = generate_pdf_report(analysis)

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="AI_Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")

st.markdown(
    "💡 Built with Python, Streamlit, Groq LLMs and ReportLab by **Shubh Beniwal**"
)