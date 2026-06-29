import hashlib
import os
from typing import List
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from supabase import create_client

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
API_KEY = os.getenv("API_KEY")

router = APIRouter(prefix="/v1/action", tags=["action"])

class ActionRequest(BaseModel):
    agent_id: str
    model: str
    authorized_by: str
    scope: List[str] = []
    prompt: str
    result: str

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def auth(x_api_key: str = Header(..., alias="x-api-key")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

@router.post("/log", status_code=201)
async def log_action(payload: ActionRequest, x_api_key: str = Header(..., alias="x-api-key")):
    auth(x_api_key)
    row = {
        "agent_id": payload.agent_id,
        "model": payload.model,
        "authorized_by": payload.authorized_by,
        "scope": payload.scope,
        "prompt_hash": sha256(payload.prompt),
        "result_hash": sha256(payload.result),
        "proof_hash": sha256(payload.prompt + payload.result),
    }
    res = supabase.table("actions").insert(row).execute()
    if not res.data:
        raise HTTPException(status_code=500, detail="Insert failed")
    return {"action_id": res.data[0]["id"], "proof_hash": res.data[0]["proof_hash"]}

@router.get("/proof/{action_id}")
async def get_proof(action_id: str, x_api_key: str = Header(..., alias="x-api-key")):
    auth(x_api_key)
    res = supabase.table("actions").select("*").eq("id", action_id).single().execute()
    if not res.data:
        raise HTTPException(status_code=404, detail="Action not found")
    return res.data
