# TMX — Truvem Memory eXchange Protocol

**Version:** 0.2  
**Status:** Draft  
**Author:** Dieng Amine (Truvem)  
**Date:** July 2026  

---

## What is TMX?

TMX (Truvem Memory eXchange) is an open, model-agnostic format for storing, exporting, and importing AI agent memories **and actions** across platforms, frameworks, and providers.

Like SMTP for email or HTTP for the web, TMX defines a **standard language** that any memory or proof system can speak — so agent memories and actions are never locked to a single vendor.

> **"Your agent's memory and actions belong to your agent — not to a vendor."**

---

## The Problem TMX Solves

Today, if you store memories in Mem0, you can't move them to Zep. If you use Letta, you can't export to Truvem. Every memory provider has a proprietary format — creating **permanent vendor lock-in**.

Worse: when AI agents **act** (send emails, approve refunds, modify configs), there is no standard way to **prove** what happened. Logs are mutable. Audit trails are inconsistent. Compliance is impossible.

TMX solves both problems.

---

## Core Principles

1. **Open** — TMX is free for anyone to implement. No license required.
2. **Model-agnostic** — Works with GPT, Claude, Gemini, Mistral, Llama, or any future model.
3. **Framework-agnostic** — Works with LangChain, CrewAI, AutoGen, or any framework.
4. **Human-readable** — Plain JSON. No binary formats. Inspectable by any tool.
5. **Portable** — Export from any provider, import to any provider.
6. **Minimal** — The spec is intentionally small. Complexity is optional.
7. **Verifiable** — Action proofs use SHA-256, append-only, tamper-evident.

---

## TMX has two parts

### Part 1 — Memory Format (TMX-M)
Portable storage and exchange of agent memories.

### Part 2 — Action Proof Format (TMX-A) ✨ NEW
Cryptographic proof of every agent action. Append-only. Verifiable forever.

---

## Part 1 — TMX Memory Format

```json
{
  "tmx_version": "0.2",
  "type": "memory",
  "exported_at": "2026-07-01T12:00:00Z",
  "source": "truvem",
  "agent_id": "my-agent",
  "memories": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "content": "User prefers dark mode and concise responses",
      "created_at": "2026-06-01T08:30:00Z",
      "updated_at": "2026-06-01T08:30:00Z",
      "expires_at": null,
      "tags": ["preference", "ui"],
      "source_model": "gpt-4o",
      "metadata": {}
    }
  ]
}
```

### Memory Field Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `tmx_version` | string | ✅ | TMX spec version |
| `type` | string | ✅ | `"memory"` |
| `exported_at` | ISO 8601 | ✅ | Timestamp of export |
| `source` | string | ✅ | Provider that exported |
| `agent_id` | string | ✅ | Agent identifier |
| `memories` | array | ✅ | List of memory objects |
| `id` | UUID | ✅ | Unique memory ID |
| `content` | string | ✅ | Memory content |
| `created_at` | ISO 8601 | ✅ | Creation timestamp |
| `expires_at` | ISO 8601 or null | ✅ | Expiration or null |
| `tags` | string[] | ❌ | Optional tags |
| `source_model` | string | ❌ | Model that created memory |

---

## Part 2 — TMX Action Proof Format ✨

```json
{
  "tmx_version": "0.2",
  "type": "action_proof",
  "action_id": "da4c5ad4-cb5a-40be-98c0-b746f1ea793c",
  "agent_id": "my-agent",
  "model": "gpt-4o",
  "authorized_by": "user@company.com",
  "scope": "web_search",
  "prompt_hash": "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969",
  "result_hash": "78ae647dc5544d227130a0682a51e30bc7777fbb6d8a8f17007463a3ecd1d524",
  "proof_hash": "872e4e50ce9990d8b041330c47c9ddd11bec6b503ae9386a99da8584e9bb12c4",
  "algorithm": "SHA-256",
  "ledger": "append-only",
  "standard": "TMX",
  "created_at": "2026-06-30T08:26:33Z"
}
```

### Action Proof Field Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `tmx_version` | string | ✅ | TMX spec version |
| `type` | string | ✅ | `"action_proof"` |
| `action_id` | UUID | ✅ | Unique action ID |
| `agent_id` | string | ✅ | Agent that acted |
| `model` | string | ✅ | LLM model used |
| `authorized_by` | string | ✅ | Who authorized the action |
| `scope` | string | ✅ | What the action was allowed to do |
| `prompt_hash` | string | ✅ | SHA-256 of the prompt |
| `result_hash` | string | ✅ | SHA-256 of the result |
| `proof_hash` | string | ✅ | SHA-256 of prompt_hash + result_hash |
| `algorithm` | string | ✅ | Always `"SHA-256"` |
| `ledger` | string | ✅ | Always `"append-only"` |
| `created_at` | ISO 8601 | ✅ | When action was logged |

### How proof_hash is computed

```python
import hashlib

proof_hash = hashlib.sha256(
    (prompt_hash + result_hash).encode()
).hexdigest()
```

Anyone can verify this independently. If `proof_hash` matches → data is intact. If not → tampered.

---

## Truvem API — TMX Support

### Log an action (creates TMX-A proof)

```bash
curl -X POST https://truvem.onrender.com/v1/action/log \
  -H "x-api-key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "my-agent",
    "model": "gpt-4o",
    "authorized_by": "user@company.com",
    "scope": ["web_search"],
    "prompt": "What is Truvem?",
    "result": "The proof layer for every AI action."
  }'
```

### Retrieve proof

```bash
curl https://truvem.onrender.com/v1/action/proof/ACTION_ID \
  -H "x-api-key: YOUR_KEY"
```

### Export memories as TMX-M

```bash
curl https://truvem.onrender.com/v1/memory/read \
  -H "x-api-key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"agent_id": "my-agent"}'
```

---

## Implementing TMX

Anyone can implement TMX. No fee. No approval. Open standard.

**TMX-M compatible** → export/import memories in valid TMX JSON format.

**TMX-A compatible** → log actions with SHA-256 proof, append-only storage, verifiable at any time.

---

## Roadmap

| Version | Features |
|---|---|
| **0.1** | Core memory format, basic fields |
| **0.2** (current) | Action proof format (TMX-A), SHA-256, append-only |
| **0.3** | Migration scripts, CLI verify tool, memory relationships |
| **1.0** | Stable standard, TMX Foundation, community governance |

---

## Why This Matters

The AI agent ecosystem is growing exponentially. Agents are moving from "answering" to "acting" — sending emails, approving payments, modifying systems.

**Two questions no one has answered yet:**
1. Who controls agent memory?
2. Who can prove what an agent did?

TMX answers both. An open standard means no single company can monopolize AI agent memory or proof.

---

## Contributing

- 📖 **Spec feedback** → Open a GitHub Issue
- 🔧 **Implementation** → Submit a PR
- 📣 **Spread** → Share with your team

**GitHub:** https://github.com/truvem/truvem  
**Email:** gettruvem@gmail.com  
**Twitter:** @gettruvem

---

## License

CC0 1.0 — Public domain. No restrictions.

---

*TMX was created by Dieng Amine, founder of Truvem, in June 2026.*  
*"The proof layer that belongs to everyone."*
