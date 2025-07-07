import faiss
import numpy as np

def build_index(embeddings: list[list[float]]) -> any:
    dim = len(embeddings[0])
    index = faiss.IndexHNSWFlat(dim, 32)
    index.add(np.array(embeddings).astype('float32'))
    return index

def save_index(index, path: str):
    faiss.write_index(index, path)

def load_index(path: str):
    return faiss.read_index(path)