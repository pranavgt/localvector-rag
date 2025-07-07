from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")  # Or your local model

    def encode(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()
