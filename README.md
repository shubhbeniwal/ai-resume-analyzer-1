# 🧠 CareerLens AI – Resume Intelligence & Job Match Analyzer

An AI-powered Resume Analyzer that evaluates resumes against job descriptions and provides intelligent feedback, skill gap analysis, and ATS-style scoring using Generative AI.

---
# 🌐 Live Demo

Example: https://ai-resume-analyzer-1-a5jjvpodez9o3vcu8ofpfr.streamlit.app/#ai-resume-analyzer

## 🚀 Features

- 📄 Upload and parse PDF resumes
- 🤖 AI-based resume analysis using LLM (Gemini/OpenAI integration)
- 🎯 ATS score estimation
- 📊 Skill gap detection based on job description
- 🧾 Clean structured output for candidates
- ⚡ Fast backend processing with Python

---

## 🏗️ Tech Stack

- Python
- FastAPI / Flask (backend)
- Gemini API / LLM integration
- PyPDF2 / PDF parsing utilities
- HTML/CSS (if frontend used)
- Git & GitHub

---

## 📂 Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── utils/
│ ├── gemini_analyzer.py
│ └── pdf_reader.py
│
└── README.md


2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the project
python app.py
🔑 Environment Variables

Create a .env file:

GROK_API_KEY=your_api_key_here
📌 How it works
User uploads resume (PDF)
System extracts text
Job description is compared using LLM
AI generates:
ATS score
Missing skills
Improvement suggestions
📊 Example Output
ATS Score: 78/100

Missing Skills:
- Docker
- System Design

Suggestions:
- Add more project details
- Highlight ML experience
📈 Future Improvements
Resume ranking system
Multi-resume comparison
Job recommendation engine
Web deployment (Render / Vercel)
User authentication system
👨‍💻 Author

Shubh Beniwal

GitHub: https://github.com/shubhbeniwal
Project: AI Resume Analyzer
⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
