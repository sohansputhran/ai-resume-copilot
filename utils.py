import pdfplumber

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    # Use basic NLP or predefined skills list; for demo, just dummy extraction
    skills_keywords = ["python", "sql", "data", "ai", "ml", "streamlit", "llm", "resume"]
    found = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return list(set(found))