from fastapi import APIRouter
from pydantic import BaseModel
from backend.pipeline.rag_chain import build_rag_chain
from fastapi.responses import StreamingResponse

router = APIRouter()
chain = build_rag_chain()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(req: ChatRequest):
    async def stream():
        for chunk in chain.stream(req.question):
            yield chunk
    return StreamingResponse(stream(), media_type="text/plain")