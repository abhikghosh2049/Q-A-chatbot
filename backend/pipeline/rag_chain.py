from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough   # changed
from langchain_core.output_parsers import StrOutputParser  # changed
from backend.ingestion.embedder import get_vectorstore
from backend.llm.prompt_templates import RAG_PROMPT
from backend.config import settings

def build_rag_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": settings.TOP_K})
    
    llm = Ollama(
        model=settings.LLM_MODEL,
        base_url=settings.OLLAMA_BASE_URL
    )

    def format_context(docs):
        return "\n\n".join(d.page_content for d in docs)

    chain = (
        {"context": retriever | format_context, "question": RunnablePassthrough()}
        | RAG_PROMPT
        | llm
        | StrOutputParser()
    )
    return chain