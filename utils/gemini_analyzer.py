# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# def analyze_resume(resume_text):

#     model = genai.GenerativeModel("gemini-2.0-flash")

#     prompt = f"""
# You are an expert ATS Resume Reviewer.

# Analyze this resume and provide:

# 1. Professional Summary
# 2. Strengths
# 3. Weaknesses
# 4. Missing Skills
# 5. Suggestions for Improvement

# Resume:

# {resume_text}
# """

#     response = model.generate_content(prompt)

#     return response.text


# from huggingface_hub import InferenceClient
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = InferenceClient(
#     token=os.getenv("HF_TOKEN")
# )


# def analyze_resume(resume_text):

#     prompt = f"""
# You are an expert ATS Resume Reviewer.

# Analyze this resume and provide:

# 1. Professional Summary
# 2. Strengths
# 3. Weaknesses
# 4. Missing Skills
# 5. Suggestions for Improvement

# Resume:

# {resume_text}
# """

#     response = client.text_generation(
#         prompt,
#         model="google/flan-t5-large",
#         max_new_tokens=500
#     )

#     return response


from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze this resume and provide:

1. Professional Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for Improvement

Resume:

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