from langchain.prompts import PromptTemplate

resume_jd_match_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
You are an AI career advisor. Based on the provided resume and job description, analyze the match between the candidate's qualifications and the job requirements.

Resume:
{resume}

Job Description:
{job_description}

Answer the following:
1. How well does the resume match the job?
2. What key skills or experiences are missing?
3. Suggest 3 resume bullet points that better align with this job.

Respond in a clear, professional tone.
"""
)