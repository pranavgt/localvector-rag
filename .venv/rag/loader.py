from pathlib import Path

def load_documents(source_dir: str) -> list[str]:
    docs = []
    for file in Path(source_dir).glob("*.txt"):
        docs.append(file.read_text())
    return docs

def chunk_documents(docs: list[str], chunk_size: int = 500) -> list[str]:
    # Simple word splitter — customize as needed
    chunks = []
    for doc in docs:
        words = doc.split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i+chunk_size])
            chunks.append(chunk)
    return chunks