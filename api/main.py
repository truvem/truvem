import os
import secrets
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from supabase import create_client
from typing import Optional

app = FastAPI()

supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

class WriteRequest(BaseModel):
    agent_id: str
    content: str

class ReadRequest(BaseModel):
    agent_id: str

class RegisterRequest(BaseModel):
    email: str

def check_key(x_api_key: Optional[str] = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key required")
    result = supabase.table("users").select("*").eq("api_key", x_api_key).execute()
    if not result.data:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return result.data[0]

@app.get("/")
def root():
    return {"name": "Truvem", "version": "0.2.0", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/v1/register")
def register(req: RegisterRequest):
    existing = supabase.table("users").select("*").eq("email", req.email).execute()
    if existing.data:
        return {"status": "ok", "api_key": existing.data[0]["api_key"]}
    api_key = "truvem_" + secrets.token_urlsafe(32)
    result = supabase.table("users").insert({
        "email": req.email,
        "api_key": api_key
    }).execute()
    return {"status": "ok", "api_key": api_key}

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
