## 📂 Project Structure

<pre>
localvector-rag/
│
├── data/
│   ├── docs/               # Raw input documents
│   └── index/              # Saved vector index files
│
├── models/
│   ├── embedding_model.py  # Embedding model wrapper
│   ├── llm_wrapper.py      # Local/private LLM wrapper
│
├── rag/
│   ├── __init__.py
│   ├── loader.py           # Load & chunk documents
│   ├── embedder.py         # Embed chunks
│   ├── indexer.py          # Build/save/load index
│   ├── retriever.py        # Retrieve relevant chunks
│   ├── generator.py        # Generate final answer
│
├── main.py                 # Entrypoint script
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── .gitignore              # Ignore local index, cache, etc.
└── Dockerfile (optional)   # Containerize if needed
</pre>
