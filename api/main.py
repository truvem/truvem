import os
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

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

@app.get("/")
def root():
    return {"name": "Truvem", "version": "0.1.0", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/v1/memory/write")
def write_memory(req: WriteRequest):
    result = supabase.table("memories").insert({
        "agent_id": req.agent_id,
        "content": req.content
    }).execute()
    return {"status": "written", "data": result.data}

@app.post("/v1/memory/read")
def read_memory(req: ReadRequest):
    result = supabase.table("memories").select("*").eq("agent_id", req.agent_id).execute()
    return {"status": "ok", "memories": result.data}
