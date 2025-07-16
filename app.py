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
    with st.spinner("🔍 Analyzing your resume and job description..."):
        resume_text = extract_text_from_pdf(resume_file)
        jd_text = extract_text_from_pdf(jd_file)

        # Skills Extraction
        resume_skills = set(extract_skills(resume_text))
        jd_skills = set(extract_skills(jd_text))

        missing_skills = jd_skills - resume_skills
        st.write("## Missing Skills (in JD but not in Resume)", missing_skills)


        # Vector DB for RAG
        vectordb = create_vectorstore([resume_text, jd_text])

        query = "Perform end-to-end resume optimization based on a job description, including gap analysis and section-wise tailoring."
        
        related_chunks = semantic_search(vectordb, query)
        context = "\n".join(related_chunks)

        prompt = f"""
            You are an expert AI resume assistant.

            Your task is to help tailor a resume for a specific job by performing the following step-by-step analysis. Use the resume and job description content provided.

            ---

            📌 Step 1: Initial Analysis
            Analyze the following job description and identify the key skills, experience, and qualifications required for the role. Present this information as a bulleted list.

            {jd_text[:1200]}...

            ---

            📌 Step 2: Resume Review
            Review the resume provided below and list the skills, experiences, and qualifications it currently highlights.

            {resume_text[:1200]}...

            ---

            📌 Step 3: Gap Analysis and Optimization
            Compare the key requirements from the job description with the resume content. Identify:
            - Any gaps in skills, qualifications, or experience
            - Areas where the resume could be improved or better aligned
            - Specific suggestions for additions, improvements, or keyword usage

            ---

            📌 Step 4: Tailoring the Resume Sections

            **Professional Summary**  
            Rewrite the professional summary section (if available) to reflect relevant skills and experiences for a [Job Title] position at [Company Name]. Emphasize the most important skills from the job description.

            **Work Experience**  
            Suggest edits to improve alignment with the job responsibilities. Focus on measurable outcomes and quantified achievements. Use action verbs and mirror the job’s key responsibilities.

            **Skills**  
            Suggest additional keywords or phrases to include in the skills section, based on the job description.

            ---

            📌 Step 5: Final Review
            Review the updated version of the resume for:
            - Clarity and conciseness
            - Impact and relevance
            - Overall polish for submission

            Be concise but specific in your recommendations. Output should be structured clearly so the user can copy and apply improvements directly.
            """

        answer = generate_response(prompt)

        # Display Results
    st.success("✅ Analysis complete!")

    if missing_skills:
        st.write("### 🧠 Missing Skills Based on JD")
        st.markdown(f"Your resume is missing some skills mentioned in the job description, such as: **{', '.join(sorted(missing_skills))}**.")
    else:
        st.write("✅ Your resume covers all the skills mentioned in the job description!")

    st.write("### 💡 AI-Powered Suggestions to Improve Resume")
    st.markdown(answer)
else:
    st.info("Please upload both your resume and job description PDFs.")

