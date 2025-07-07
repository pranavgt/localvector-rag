def embed_chunks(chunks, model):
    embeddings = []
    for chunk in chunks:
        emb = model.encode(chunk)
        embeddings.append(emb)
    return embeddings