from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore(texts, embedding_model_name='sentence-transformers/all-MiniLM-L6-v2'):
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    docs = splitter.create_documents(texts)
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectordb = FAISS.from_documents(docs, embeddings)
    return vectordb

def semantic_search(vectordb, query, k=4):
    results = vectordb.similarity_search(query, k=k)
    return [r.page_content for r in results]