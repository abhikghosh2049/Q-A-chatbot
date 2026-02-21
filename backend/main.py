from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.routers import chat, ingest
from backend.ingestion.auto_ingest import auto_ingest_all

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up — auto-ingesting documents...")
    auto_ingest_all()
    yield

app = FastAPI(title="RAG Chatbot API", lifespan=lifespan)
app.include_router(chat.router)
app.include_router(ingest.router)