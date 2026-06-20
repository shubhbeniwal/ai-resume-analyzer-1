from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, job_description=""):

    prompt = f"""
You are a senior ATS Resume Reviewer and Technical Recruiter.

Analyze the resume against the provided job description.

Provide your response in EXACTLY the following format:

ATS Match Score: <score out of 100>

## Professional Summary
<summary>

## Matching Skills
- skill 1
- skill 2
- skill 3

## Missing Skills
- skill 1
- skill 2

## Strengths
- point 1
- point 2

## Suggestions for Improvement
- suggestion 1
- suggestion 2
- suggestion 3

Rules:
- ATS Match Score must be between 0 and 100.
- Only list skills as "Missing Skills" if they are clearly absent from the resume.
- If a skill is present through certifications, projects, experience, or coursework, treat it as a matching skill.
- Do not explain missing skills inside the skill name.
- Return clean bullet points only.

JOB DESCRIPTION:

{job_description}

RESUME:

{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content