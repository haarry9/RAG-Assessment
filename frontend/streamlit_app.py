# simple chat frontend for fastapi backend rag
import streamlit as st
from .schemas import QueryRequest
from .pipeline import query_rag

st.title("HR Docs RAG Chat")

question = st.text_input("Enter your question")
if st.button("Ask"):
    answer = query_rag(question)
    st.write(answer)