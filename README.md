# 🧠 Q-A Chatbot

**RAG Q&A Chatbot — Open-Source LLM-Powered Document Question-Answering System**

This project is a Retrieval-Augmented Generation (RAG) chatbot that lets you upload documents and ask questions about them using large language models (LLMs). It runs **fully locally** with privacy-first design — no cloud APIs required and no data ever leaves your machine.

---

## 🚀 Features

- 📄 **Document Q&A:** Upload PDFs, Word docs, text, and ask questions based on content.
- 🤖 **LLM Powered:** Uses open-source Llama 2 locally for answer generation.
- ⚡ **Fast Retrieval:** Embeddings + Vector store (Chroma) for efficient semantic search.
- 🧩 **RAG Pipeline:** LangChain orchestrates retrieval and response generation.
- 🖥️ **Frontend UI:** Streamlit interface for easy interactions.
- 🛠️ **Backend API:** FastAPI for backend logic and vector ingestion.

---

## 🧱 Tech Stack

| Component        | Technology |
|------------------|------------|
| LLM              | Llama 2 via Ollama |
| Embeddings       | nomic-embed-text |
| Vector Store     | ChromaDB |
| Orchestration    | LangChain |
| Backend          | FastAPI |
| Frontend         | Streamlit |
| Document Parser  | PyMuPDF, python-docx |

---

## 📦 Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.10 or higher
- Ollama (for running LLM locally)
- Optional (for Word support): Node.js

---

## 🛠️ Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/abhikghosh2049/Q-A-chatbot.git
   cd Q-A-chatbot
