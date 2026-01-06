"""
Endpoints base
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

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
    # Lógica para responder preguntas
    return {
        "question": request.question,
        "answer": "This is a placeholder response from the GenAI service.",
    }
@router.get("/health")
def health_check():
    return {"status": "healthy"}