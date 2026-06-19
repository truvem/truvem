import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from supabase import create_client
from typing import Optional

app = FastAPI()

supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

API_KEY = os.environ.get("API_KEY", "truvem_test_123")

class WriteRequest(BaseModel):
    agent_id: str
    content: str

class ReadRequest(BaseModel):
    agent_id: str

def check_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.get("/")
def root():
    return {"name": "Truvem", "version": "0.1.0", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/v1/memory/write")
def write_memory(req: WriteRequest, x_api_key: Optional[str] = Header(None)):
    check_key(x_api_key)
    result = supabase.table("memories").insert({
        "agent_id": req.agent_id,
        "content": req.content
    }).execute()
    return {"status": "ok", "data": result.data}

@app.post("/v1/memory/read")
def read_memory(req: ReadRequest, x_api_key: Optional[str] = Header(None)):
    check_key(x_api_key)
    result = supabase.table("memories").select("*").eq("agent_id", req.agent_id).execute()
    return {"status": "ok", "memories": result.data}
