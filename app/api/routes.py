"""
Endpoints base
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.rag.knowledge import vector_store
from app.rag.prompt import build_prompt
from app.llm.client import generate_answer

router = APIRouter()

class IngestRequest(BaseModel):
    documents: List[str]

class AskRequest(BaseModel):
    question: str

@router.post("/ingest")
def ingest_docs(request: IngestRequest):
    """
    Endpoint para ingerir documentos.
    """
    # Lógica para ingerir documentos
    return {"status": "OK", "Documents Received": len(request.documents)}

@router.post("/ask")
def ask_question(request: AskRequest):
    """
    Endpoint para hacer preguntas.
    """
    context = vector_store.search(request.question)
    prompt = build_prompt(request.question, context)
    answer = (generate_answer(prompt)
    )
    # Lógica para responder preguntas
    return {
        "question": request.question,
        "context": context,
        "answer": answer
    }
@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.get("/ready")
def readiness():
    # acá más adelante podés chequear:
    # - vector store
    # - modelo cargado
    # - conexión externa
    return {"status": "ready"}