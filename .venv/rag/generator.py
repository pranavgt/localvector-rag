from models.llm_wrapper import call_llm

def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return call_llm(prompt)