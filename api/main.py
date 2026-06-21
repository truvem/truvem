import os
import secrets
from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from supabase import create_client
from typing import Optional

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
@limiter.limit("60/minute")
def root(request: Request):
    return {"name": "Truvem", "version": "0.2.0", "status": "ok"}

@app.api_route("/health", methods=["GET", "HEAD"])
@limiter.limit("60/minute")
def health(request: Request):
    return {"status": "healthy"}

@app.post("/v1/register")
@limiter.limit("10/minute")
def register(request: Request, req: RegisterRequest):
    existing = supabase.table("users").select("*").eq("email", req.email).execute()
    if existing.data:
        return {"status": "ok", "api_key": existing.data[0]["api_key"]}
    api_key = "truvem_" + secrets.token_urlsafe(32)
    supabase.table("users").insert({
        "email": req.email,
        "api_key": api_key
    }).execute()
    return {"status": "ok", "api_key": api_key}

@app.post("/v1/memory/write")
@limiter.limit("100/minute")
def write_memory(request: Request, req: WriteRequest, x_api_key: Optional[str] = Header(None)):
    check_key(x_api_key)
    result = supabase.table("memories").insert({
        "agent_id": req.agent_id,
        "content": req.content
    }).execute()
    return {"status": "ok", "data": result.data}

@app.post("/v1/memory/read")
@limiter.limit("100/minute")
def read_memory(request: Request, req: ReadRequest, x_api_key: Optional[str] = Header(None)):
    check_key(x_api_key)
    result = supabase.table("memories").select("*").eq("agent_id", req.agent_id).execute()
    return {"status": "ok", "memories": result.data}
