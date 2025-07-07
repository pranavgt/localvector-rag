import numpy as np

def retrieve(query, model, index, chunks, top_k=5):
    query_emb = np.array(model.encode(query)).astype('float32')
    distances, indices = index.search(query_emb.reshape(1, -1), top_k)
    return [chunks[i] for i in indices[0]]