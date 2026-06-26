# TMX — Truvem Memory eXchange Protocol

**Version:** 0.1  
**Status:** Draft  
**Author:** Dieng Amine (Truvem)  
**Date:** June 2026  

---

## What is TMX?

TMX (Truvem Memory eXchange) is an open, model-agnostic format for storing, exporting, and importing AI agent memories across platforms, frameworks, and providers.

Like SMTP for email or HTTP for the web, TMX defines a **standard language** that any memory system can speak — so agent memories are never locked to a single vendor.

> **"Your agent's memory belongs to your agent — not to a vendor."**

---

## The Problem TMX Solves

Today, if you store memories in Mem0, you can't move them to Zep. If you use Letta, you can't export to Truvem. Every memory provider has a proprietary format — creating **permanent vendor lock-in**.

This is exactly the problem email had before SMTP, and the web had before HTTP.

TMX is the missing standard.

---

## Core Principles

1. **Open** — TMX is free for anyone to implement. No license required.
2. **Model-agnostic** — Works with GPT, Claude, Gemini, Mistral, Llama, or any future model.
3. **Framework-agnostic** — Works with LangChain, CrewAI, Mastra, AutoGen, or any framework.
4. **Human-readable** — Plain JSON. No binary formats. Inspectable by any tool.
5. **Portable** — Export from any provider, import to any provider.
6. **Minimal** — The spec is intentionally small. Complexity is optional, not required.

---

## The TMX Format

A TMX file is a JSON document with the following structure:

```json
{
  "tmx_version": "0.1",
  "exported_at": "2026-06-25T12:00:00Z",
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

---

## Field Reference

### Root fields

| Field | Type | Required | Description |
|---|---|---|---|
| `tmx_version` | string | ✅ | TMX spec version (e.g. `"0.1"`) |
| `exported_at` | ISO 8601 | ✅ | Timestamp of export |
| `source` | string | ✅ | Provider that exported this file (e.g. `"truvem"`, `"mem0"`) |
| `agent_id` | string | ✅ | Unique identifier for the agent |
| `memories` | array | ✅ | List of memory objects |

### Memory object fields

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | UUID | ✅ | Unique memory identifier |
| `content` | string | ✅ | The memory content (plain text) |
| `created_at` | ISO 8601 | ✅ | When this memory was created |
| `updated_at` | ISO 8601 | ✅ | When this memory was last updated |
| `expires_at` | ISO 8601 or null | ✅ | Expiration timestamp, or null for permanent |
| `tags` | array of strings | ❌ | Optional categorization tags |
| `source_model` | string | ❌ | LLM model that generated this memory |
| `metadata` | object | ❌ | Any provider-specific extra data |

---

## Example: Full TMX File

```json
{
  "tmx_version": "0.1",
  "exported_at": "2026-06-25T14:32:00Z",
  "source": "truvem",
  "agent_id": "customer-support-bot",
  "memories": [
    {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "content": "User's name is Sarah. She is a premium subscriber since March 2025.",
      "created_at": "2026-05-10T09:00:00Z",
      "updated_at": "2026-05-10T09:00:00Z",
      "expires_at": null,
      "tags": ["user-profile", "subscription"],
      "source_model": "claude-sonnet-4-5",
      "metadata": {}
    },
    {
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "content": "Sarah prefers email over phone for support. Timezone: UTC+1.",
      "created_at": "2026-05-15T11:30:00Z",
      "updated_at": "2026-05-15T11:30:00Z",
      "expires_at": null,
      "tags": ["preference", "contact"],
      "source_model": "gpt-4o",
      "metadata": {}
    }
  ]
}
```

---

## Truvem API — TMX Support

Truvem supports TMX natively:

### Export memories as TMX

```bash
curl -X GET https://truvem.onrender.com/v1/memory/export?agent_id=my-agent \
  -H "x-api-key: your_key"
```

Response: a valid `.tmx.json` file.

### Import a TMX file

```bash
curl -X POST https://truvem.onrender.com/v1/memory/import \
  -H "x-api-key: your_key" \
  -H "Content-Type: application/json" \
  -d @my-memories.tmx.json
```

---

## Migration Scripts

Move your memories from other providers to Truvem in one command:

```bash
# From Mem0
python scripts/migrate_mem0.py --api-key YOUR_KEY

# From Zep
python scripts/migrate_zep.py --api-key YOUR_KEY
```

*(Scripts coming in TMX 0.2)*

---

## Implementing TMX

Anyone can implement TMX. To be listed as a **TMX-compatible provider**, your system must:

1. Export memories in valid TMX JSON format
2. Import valid TMX JSON files without data loss
3. Preserve all required fields (`id`, `content`, `created_at`, `updated_at`, `expires_at`)

That's it. No fee. No approval needed. Open standard.

---

## Roadmap

| Version | Features |
|---|---|
| **0.1** (current) | Core format, basic fields, export/import |
| **0.2** | Migration scripts (Mem0, Zep, Letta), CLI tool |
| **0.3** | Memory relationships, superseding (temporal invalidation) |
| **1.0** | Stable standard, community governance, TMX Foundation |

---

## Why This Matters

The AI agent ecosystem is growing exponentially. In 10 years, there will be more AI agents running than humans on Earth. Every one of them will need memory.

The question is: **who controls that memory?**

If every vendor uses a proprietary format, agent memories are forever fragmented — locked to whoever built the tool the developer happened to choose first.

TMX is the answer. An open standard means:
- Developers can switch providers without losing memories
- Agents can be truly portable across clouds and frameworks
- No single company can monopolize AI agent memory

---

## Contributing

TMX is open. Contributions welcome:

- 📖 **Spec feedback** → Open a GitHub Issue
- 🔧 **Implementation** → Submit a PR with your TMX-compatible library
- 📣 **Spread the word** → Share this spec with your team

**GitHub:** https://github.com/truvem/truvem  
**Email:** gettruvem@gmail.com  
**Twitter:** @gettruvem

---

## License

The TMX specification is released under **Creative Commons CC0 1.0** — public domain. No restrictions. Implement it freely, commercially or otherwise.

---

*TMX was created by Dieng Amine, founder of Truvem, in June 2026.*  
*"The memory layer that belongs to everyone."*
