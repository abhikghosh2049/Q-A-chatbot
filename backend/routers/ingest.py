from fastapi import APIRouter, UploadFile, File
import shutil
from backend.ingestion.document_loader import load_documents
from backend.ingestion.text_splitter import split_documents
from backend.ingestion.embedder import ingest_documents
from backend.ingestion.auto_ingest import auto_ingest_all

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    save_path = f"./data/documents/{file.filename}"
    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    docs = load_documents(save_path)
    chunks = split_documents(docs)
    count = ingest_documents(chunks)
    return {"message": f"Ingested {count} chunks from {file.filename}"}

@router.post("/ingest-all")
async def ingest_all():
    auto_ingest_all()
    return {"message": "Re-ingestion from data/documents/ complete."}