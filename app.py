import streamlit as st
from llm_local import generate_response
from retriever import create_vectorstore, semantic_search
from utils import extract_text_from_pdf, extract_skills

st.set_page_config(page_title="AI Resume Copilot", layout="wide")

st.title("AI Resume Copilot")

st.sidebar.header("Upload your files")
resume_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.sidebar.file_uploader("Upload Job Description (PDF)", type=["pdf"])

if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    # Skills Extraction
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    st.write("## Extracted Resume Skills", resume_skills)
    st.write("## Extracted JD Skills", jd_skills)

    # Vector DB for RAG
    vectordb = create_vectorstore([resume_text, jd_text])

    query = st.text_input("Ask something about your fit to this job:", value="What are the top gaps between my resume and the job description?")

    if st.button("Analyze"):
        related_chunks = semantic_search(vectordb, query)
        context = "\n".join(related_chunks)
        prompt = f"""Given the following RESUME and JOB DESCRIPTION, answer the user's question.

RESUME:
{resume_text[:1200]}...

JOB DESCRIPTION:
{jd_text[:1200]}...

Relevant Info:
{context}

Question: {query}
"""
        answer = generate_response(prompt)
        st.write("### AI Analysis", answer)
else:
    st.info("Please upload both your resume and job description PDFs.")

# Extra: Display file contents (optional, for debug)
# st.expander("Resume Text").write(resume_text[:1000])
# st.expander("Job Description Text").write(jd_text[:1000])