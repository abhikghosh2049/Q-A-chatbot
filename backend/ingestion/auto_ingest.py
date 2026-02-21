import os
from backend.ingestion.document_loader import load_documents
from backend.ingestion.text_splitter import split_documents
from backend.ingestion.embedder import ingest_documents, get_vectorstore

DOCUMENTS_DIR = "./data/documents"

def auto_ingest_all():
    supported = (".pdf", ".txt", ".docx")
    files = [
        f for f in os.listdir(DOCUMENTS_DIR)
        if f.lower().endswith(supported)
    ]

    if not files:
        print("No documents found in data/documents/")
        return

    # Check already ingested to avoid duplicates
    vs = get_vectorstore()
    existing = vs.get()["metadatas"]
    already_ingested = {m.get("source", "") for m in existing if m}

    new_files = []
    for f in files:
        full_path = os.path.join(DOCUMENTS_DIR, f)
        if full_path not in already_ingested:
            new_files.append(full_path)

    if not new_files:
        print("All documents already ingested.")
        return

    total = 0
    for path in new_files:
        print(f"Ingesting: {path}")
        docs = load_documents(path)
        chunks = split_documents(docs)
        ingest_documents(chunks)
        total += len(chunks)
        print(f"  → {len(chunks)} chunks added")

    print(f"Auto-ingestion complete: {total} total chunks from {len(new_files)} files.")