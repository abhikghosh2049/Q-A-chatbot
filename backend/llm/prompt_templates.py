from langchain_core.prompts import ChatPromptTemplate  # changed

RAG_PROMPT = ChatPromptTemplate.from_template("""
You are a helpful Q&A assistant. Answer the user's question using ONLY the 
provided context. If the answer is not in the context, say "I don't know 
based on the provided documents."

Context:
{context}

Question: {question}

Answer:
""")