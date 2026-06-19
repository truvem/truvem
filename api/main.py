from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid
import time

app = FastAPI(title="Truvem API", version="0.1.0")

# Stockage en mémoire pour le MVP
db = {}

class MemoryWrite(BaseModel):
    agent_id: str
    content: str
    memory_type: str = "episodic"

class MemoryRead(BaseModel):
    agent_id: str
    query: str
    top_k: int = 5

@app.get("/")
def root():
    return {"name": "Truvem", "version": "0.1.0", "status": "ok"}

@app.post("/v1/memory/write")
def write_memory(req: MemoryWrite):
    memory_id = str(uuid.uuid4())
    if req.agent_id not in db:
        db[req.agent_id] = []
    db[req.agent_id].append({
        "id": memory_id,
        "content": req.content,
        "type": req.memory_type,
        "timestamp": time.time()
    })
    return {"memory_id": memory_id, "status": "written"}

@app.post("/v1/memory/read")
def read_memory(req: MemoryRead):
    memories = db.get(req.agent_id, [])
    results = [m for m in memories if req.query.lower() in m["content"].lower()]
    return {"memories": results[:req.top_k], "count": len(results)}

@app.get("/health")
def health():
    return {"status": "ok"}
