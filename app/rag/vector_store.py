import numpy as np
from sentence_transformers import SentenceTransformer

class InMemoryVectorStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.text = []
        self.embeddings = []

    def add_text(self, text: list[str]):
        vectors = self.model.encode(text)
        self.embeddings.extend(vectors)
        self.text.extend(text)

    def search(self, query: str, top_k: int = 5) -> list[str]:
        query_vec = self.model.encode([query])[0]
        sims = np.dot(self.embeddings, query_vec) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
        )
        top_indices = np.argsort(sims)[-top_k:][::-1]
        return [self.text[i] for i in top_indices]
    
    