from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    LLM_MODEL: str = "llama2"   
    EMBED_MODEL: str = "nomic-embed-text"
    CHROMA_PERSIST_DIR: str = "./vectorstore"
    COLLECTION_NAME: str = "rag_docs"
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 64
    TOP_K: int = 5

settings = Settings()