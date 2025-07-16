import pdfplumber

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    # Use basic NLP or predefined skills list
    skills_keywords = {
            'programming': {
                'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
                'scala', 'kotlin', 'swift', 'r', 'matlab', 'sql', 'html', 'css', 'html5', 'css3'
            },
            'frameworks': {
                'django', 'flask', 'fastapi', 'react', 'angular', 'vue', 'node.js', 'express',
                'spring', 'laravel', 'rails', 'pytorch', 'tensorflow', 'keras', 'scikit-learn',
                'pandas', 'numpy', 'streamlit', 'ionic', '.net', 'asp.net'
            },
            'databases': {
                'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'cassandra',
                'oracle', 'sql server', 'sqlite', 'snowflake', 'bigquery'
            },
            'cloud': {
                'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes', 'jenkins',
                'terraform', 'ansible', 'git', 'gitlab', 'github', 'bitbucket'
            },
            'data_science': {
                'machine learning', 'deep learning', 'neural networks', 'nlp', 'computer vision',
                'data analysis', 'statistics', 'big data', 'hadoop', 'spark', 'pyspark',
                'tableau', 'power bi', 'matplotlib', 'seaborn', 'plotly'
            },
            'tools': {
                'jira', 'confluence', 'slack', 'trello', 'notion', 'postman', 'swagger',
                'vs code', 'intellij', 'eclipse', 'vim', 'emacs', 'jupyter', 'airflow'
            }
        }
    found = [skill for category in skills_keywords.values() \
             for skill in category if skill.lower() in text.lower()]
    return list(set(found))