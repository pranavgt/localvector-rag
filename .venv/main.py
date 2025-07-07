from models.embedding_model import EmbeddingModel
from rag.loader import load_documents, chunk_documents
from rag.embedder import embed_chunks
from rag.indexer import build_index, save_index, load_index
from rag.retriever import retrieve
from rag.generator import generate_answer
import os

def main():
    docs = load_documents("data/docs")
    chunks = chunk_documents(docs)

    model = EmbeddingModel()
    embeddings = embed_chunks(chunks, model)

    index_path = "data/index/docs.index"

    if os.path.exists(index_path):
        index = load_index(index_path)
    else:
        index = build_index(embeddings)
        save_index(index, index_path)

    while True:
        query = input("Ask me something: ")
        relevant = retrieve(query, model, index, chunks)
        answer = generate_answer(query, relevant)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()