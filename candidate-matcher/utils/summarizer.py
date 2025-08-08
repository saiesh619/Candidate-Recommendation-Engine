import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_summary(job_text, resume_text):
    prompt = f"""Given the following job description and candidate resume, explain in 1–2 lines why the candidate is a strong match. Give Pros and Cons of candidate based on resume information 
Job Description:
{job_text}

Candidate Resume:
{resume_text}

Summary:"""
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content.strip()
