# Proof-Your-Agent

## Add cryptographic proof to your AI agent in 2 lines

[![Powered by Truvem](https://raw.githubusercontent.com/truvem/truvem/main/badge-1.svg)](https://truvem.github.io/truvem)

Every AI action should be:
- ✅ **Logged** — timestamp, agent, model, context
- ✅ **Authorized** — who approved, what scope
- ✅ **Verifiable** — SHA-256, append-only, forever

**Truvem is the proof layer for every AI action.**

---

## Install

```bash
pip install truvem
```

---

## Quick Start

```python
from truvem import Truvem

client = Truvem(api_key="YOUR_TRUVEM_KEY")

# Your agent runs a tool
result = your_tool(prompt)

# 2 lines to add cryptographic proof
response = client.log_action(
    agent_id="my-agent",
    model="gpt-4o",
    authorized_by="user@company.com",
    prompt=prompt,
    result=result
)

print(response["action_id"])   # da4c5ad4-...
print(response["proof_hash"])  # 872e4e50-...
```

---

## How it works

```
Your agent executes a tool
        ↓
Truvem hashes prompt + result (SHA-256)
        ↓
Stored in append-only ledger (no UPDATE/DELETE possible)
        ↓
You receive: action_id + proof_hash
        ↓
Anyone can verify integrity at any time
```

---

## Verify a proof

```bash
python verify.py YOUR_ACTION_ID
```

Output:
```
✅ VALID — proof is intact and untampered.
```

---

## API (curl)

```bash
# Log an action
curl -X POST https://truvem.onrender.com/v1/action/log \
  -H "x-api-key: YOUR_TRUVEM_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "my-agent",
    "model": "gpt-4o",
    "authorized_by": "user@company.com",
    "scope": ["web_search"],
    "prompt": "What is Truvem?",
    "result": "The proof layer for every AI action."
  }'

# Get proof
curl https://truvem.onrender.com/v1/action/proof/ACTION_ID \
  -H "x-api-key: YOUR_TRUVEM_KEY"
```

---

## TMX Format

```json
{
  "id": "da4c5ad4-cb5a-40be-98c0-b746f1ea793c",
  "agent_id": "my-agent",
  "model": "gpt-4o",
  "authorized_by": "user@company.com",
  "scope": "web_search",
  "prompt_hash": "185f8db3...",
  "result_hash": "78ae647d...",
  "proof_hash": "872e4e50...",
  "created_at": "2026-06-30T08:26:33Z"
}
```

TMX is an open standard for AI action portability.
Spec: [github.com/truvem/truvem/blob/main/TMX.md](https://github.com/truvem/truvem/blob/main/TMX.md)

---

## Get your free API key

[truvem.github.io/truvem](https://truvem.github.io/truvem)
