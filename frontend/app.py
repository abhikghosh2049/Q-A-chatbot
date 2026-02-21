import streamlit as st
import requests

st.title("📚 RAG Q&A Chatbot")

with st.sidebar:
    st.header("Upload Documents")
    uploaded = st.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
    if uploaded and st.button("Ingest File"):
        res = requests.post(
            "http://localhost:8000/ingest",
            files={"file": (uploaded.name, uploaded, uploaded.type)}
        )
        st.success(res.json()["message"])

    st.divider()
    st.header("Bulk Ingest from data/documents/")
    if st.button("🔄 Re-ingest All Documents"):
        res = requests.post("http://localhost:8000/ingest-all")
        st.success(res.json()["message"])

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if question := st.chat_input("Ask a question about your documents..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    with st.chat_message("assistant"):
        with requests.post(
            "http://localhost:8000/chat",
            json={"question": question},
            stream=True
        ) as res:
            answer = st.write_stream(res.iter_content(chunk_size=None, decode_unicode=True))

    st.session_state.messages.append({"role": "assistant", "content": answer})