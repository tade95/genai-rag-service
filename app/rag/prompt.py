def build_prompt(question: str, context: list[str]) -> str:
    context_block = "\n".join(context)

    return f"""
You are answering based ONLY on the context below.

Context:
{context_block}

Question:
{question}

Answer:
"""
