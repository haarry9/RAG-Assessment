# set up chromadb database for langchain rag 
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from .config import GEMINI_API_KEY, CHROMA_DB_DIR

def get_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )
    return Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)