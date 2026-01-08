from app.rag.vector_store import InMemoryVectorStore

vector_store = InMemoryVectorStore()

def load_knowledge():
    docs = [
        "FastAPI is a modern Python web framework.",
        "RAG stands for Retrieval Augmented Generation.",
        "Docker allows packaging applications into containers.",
        "CI/CD automates build and deployment pipelines."
    ]
    vector_store.add_text(docs)