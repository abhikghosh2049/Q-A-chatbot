# Q-A-chatbot
RAG Q&A Chatbot
Open-Source LLM Powered Document Q&A System

Stack: Llama 2 • Ollama • LangChain • ChromaDB • FastAPI • Streamlit

Overview
This project is a fully local, privacy-first Retrieval-Augmented Generation (RAG) chatbot that lets you upload your own documents and ask questions about them. It uses open-source LLMs running locally via Ollama, so no data ever leaves your machine.

Tech Stack
Component	Technology	Purpose
LLM	Llama 2 (via Ollama)	Answer generation
Embeddings	nomic-embed-text	Document vectorization
Vector Store	ChromaDB	Similarity search
Orchestration	LangChain	RAG pipeline
Backend	FastAPI	REST API server
Frontend	Streamlit	Chat UI
Parsing	PyMuPDF / Docx2txt	Document loading

Prerequisites
•	Python 3.10 or higher
•	Node.js (optional, for docx generation)
•	Ollama installed and running
•	8GB+ RAM recommended (16GB for Llama 2 13B)
•	4-6GB free disk space for model weights

Installation
1. Clone the Repository
git clone https://github.com/youruser/rag-chatbot.git
cd rag-chatbot

2. Create Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

3. Install Python Dependencies
pip install fastapi uvicorn langchain langchain-core langchain-community
pip install langchain-chroma langchain-ollama langchain-text-splitters
pip install chromadb sentence-transformers pymupdf python-docx
pip install unstructured python-multipart pydantic streamlit python-dotenv

4. Install & Configure Ollama
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh   # Linux/macOS
# Windows: download installer from https://ollama.com

# Pull required models
ollama pull llama2
ollama pull nomic-embed-text

# Optional: better quality models
ollama pull llama2:13b

Project Structure
rag-chatbot/
├── backend/
│   ├── main.py                  # FastAPI entry point + auto-ingest on startup
│   ├── config.py                # Settings (model names, chunk size, etc.)
│   ├── ingestion/
│   │   ├── document_loader.py   # PDF, DOCX, TXT loading
│   │   ├── text_splitter.py     # Recursive character chunking
│   │   ├── embedder.py          # Embed & store in ChromaDB
│   │   └── auto_ingest.py       # Auto-ingest from data/documents/
│   ├── retrieval/
│   │   └── retriever.py         # Vector similarity search
│   ├── llm/
│   │   ├── ollama_client.py     # Ollama LLM interface
│   │   └── prompt_templates.py  # RAG system prompt
│   ├── pipeline/
│   │   └── rag_chain.py         # Full LangChain RAG pipeline
│   └── routers/
│       ├── chat.py              # POST /chat (streaming)
│       └── ingest.py            # POST /ingest, POST /ingest-all
├── frontend/
│   └── app.py                   # Streamlit chat UI
├── data/
│   └── documents/               # Drop your docs here for auto-ingestion
├── vectorstore/                 # ChromaDB persisted data
├── .env
├── requirements.txt
└── README.md

Configuration
Edit backend/config.py to change model or chunking settings:

OLLAMA_BASE_URL = 'http://localhost:11434'
LLM_MODEL       = 'llama2'          # or 'llama2:13b', 'llama2:70b'
EMBED_MODEL     = 'nomic-embed-text'
CHROMA_PERSIST  = './vectorstore'
CHUNK_SIZE      = 512
CHUNK_OVERLAP   = 64
TOP_K           = 5                 # chunks retrieved per query

Running the Application
Step 1 — Add Your Documents
Drop any PDF, TXT, or DOCX files into the data/documents/ folder. They will be automatically ingested when the server starts.

Step 2 — Start Ollama
ollama serve

Step 3 — Start the FastAPI Backend
uvicorn backend.main:app --reload --port 8000
The server auto-ingests all documents in data/documents/ on startup. Already-ingested files are skipped automatically.

Step 4 — Start the Streamlit Frontend
streamlit run frontend/app.py
Open http://localhost:8501 in your browser.

API Reference
Method	Endpoint	Description
POST	/chat	Stream answer from RAG pipeline
POST	/ingest	Upload & ingest a single file
POST	/ingest-all	Re-ingest all docs from data/documents/

Example Chat Request
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is federated learning?"}'

Llama 2 Model Options
Model	VRAM Required	Best For
llama2 (7B)	4–6 GB	Low-resource machines, fast responses
llama2:13b	8–10 GB	Better reasoning and accuracy
llama2:70b	40+ GB	Near GPT-4 quality (requires server GPU)
llama2-uncensored	4–6 GB	Less filtered responses

Troubleshooting
ModuleNotFoundError: No module named 'langchain.schema'
LangChain moved core modules. Install the correct packages:
pip install langchain-core langchain-ollama langchain-text-splitters

ModuleNotFoundError: No module named 'langchain.text_splitter'
pip install langchain-text-splitters

OllamaEmbeddings / Ollama deprecation warnings
pip install -U langchain-ollama
# Then use: from langchain_ollama import OllamaEmbeddings, OllamaLLM

Chatbot says 'I don't know based on the provided documents'
The document has not been ingested yet. Either place it in data/documents/ and restart the server, or use the 'Ingest File' button in the sidebar, or click 'Re-ingest All Documents'.

Ollama connection refused
ollama serve   # Make sure Ollama is running first

Correct Import Reference (LangChain 0.3+)
Old (deprecated)	New (correct)
langchain.text_splitter	langchain_text_splitters
langchain_community.embeddings.OllamaEmbeddings	langchain_ollama.OllamaEmbeddings
langchain_community.llms.Ollama	langchain_ollama.OllamaLLM
langchain.schema.runnable	langchain_core.runnables
langchain.schema.output_parser	langchain_core.output_parsers
langchain.prompts	langchain_core.prompts

License
MIT License — free to use, modify, and distribute.
