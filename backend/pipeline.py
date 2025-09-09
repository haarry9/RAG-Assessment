from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from .db import get_vectorstore
from .config import GEMINI_API_KEY

def build_rag():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0
    )
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def query_rag(question: str):
    qa = build_rag()
    return qa.run(question)
                                 