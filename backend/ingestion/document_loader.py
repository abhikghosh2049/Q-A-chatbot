from langchain_community.document_loaders import (
    PyMuPDFLoader, Docx2txtLoader, TextLoader, DirectoryLoader
)

def load_documents(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyMuPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    else:
        loader = TextLoader(file_path)
    return loader.load()