from fastapi import FastAPI
from .schemas import QueryRequest, QueryResponse
from .pipeline import query_rag

app = FastAPI(title="HR Docs RAG API")

@app.post("/query", response_model=QueryResponse)
async def query_docs(req: QueryRequest):
    answer = query_rag(req.question)
    return QueryResponse(answer=answer)
~                                         