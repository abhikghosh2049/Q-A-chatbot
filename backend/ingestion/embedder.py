from langchain_ollama import OllamaEmbeddings                # changed
from langchain_chroma import Chroma
from backend.config import settings

def get_vectorstore():
    embeddings = OllamaEmbeddings(
        model=settings.EMBED_MODEL,
        base_url=settings.OLLAMA_BASE_URL
    )
    return Chroma(
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=settings.CHROMA_PERSIST_DIR
    )

def ingest_documents(chunks):
    vs = get_vectorstore()
    vs.add_documents(chunks)
    return len(chunks)