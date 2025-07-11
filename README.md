# 🧠 AI Resume Copilot

**AI Resume Copilot** is a smart assistant that analyzes your resume and a target job description using **Retrieval-Augmented Generation (RAG)** to provide actionable feedback, tailored suggestions, and skills alignment insights. It leverages **LangChain**, **FAISS**, and open-source **LLMs** to help you fine-tune your resume for maximum impact.

---

<!-- ## 📛 Badges

![Build Status](https://img.shields.io/github/actions/workflow/status/sohansputhran/ai-resume-copilot/main.yml)
![License](https://img.shields.io/github/license/sohansputhran/ai-resume-copilot)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b) 

---    -->

## 🔍 What it Does

Upload your **resume** and a **job description**, and the AI Copilot will:
- ✅ Identify key matching skills and gaps
- 💬 Answer questions like: “How well does my resume match this job?”
- 🛠 Suggest improvements and bullet points
- 🧠 Use a RAG pipeline for accurate, context-aware insights

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://www.langchain.com/) | Orchestrates the RAG pipeline and agents |
| [FAISS](https://github.com/facebookresearch/faiss) | Semantic search and vector storage |
| [Streamlit](https://streamlit.io/) | Fast, interactive frontend |
| [Open-source LLM](https://huggingface.co/models) | Natural language understanding and generation |
| Python 3.11 | Core backend logic |

---

## 🚀 Demo

📺 Coming soon: [Watch demo](#)  
<!-- 🌐 Try it live: [Streamlit Share](#) *(optional)* -->

---

## 🧭 Architecture Diagram

![Architecture Diagram](assets/architecture_diagram.png)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-resume-copilot.git
cd ai-resume-copilot
pip install -r requirements.txt
streamlit run app/main.py
```

---

## 📁 Project Structure

```
ai-resume-copilot/
├── app/               # Streamlit UI
│   └── main.py
├── rag/               # RAG and agent logic
│   ├── retriever.py
│   └── prompt_templates.py
├── data/              # Sample resumes and job descriptions
├── tests/             # Unit tests
├── assets/            # Screenshots, diagrams
├── requirements.txt
└── README.md
```

---

## ✅ Features

- 📄 PDF/DOCX upload for resumes and job descriptions
- 🔎 Semantic similarity matching with FAISS
- 🤖 Conversational Q&A agent
- ✍️ Auto-suggestions for resume bullet points
- 📊 ATS keyword alignment score *(coming soon)*

---

## 💡 Future Improvements

- Resume rewriting tool with LLM
- Multi-resume comparison
- Auto-generated cover letters
- LinkedIn JD scraping

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.  
If you find this useful, consider ⭐ starring the repo!

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

📧 Sohan Puthran  
🌐 [Portfolio Website](https://sohansputhran.github.io)  
🔗 [LinkedIn](https://www.linkedin.com/in/sohan-puthran/)
