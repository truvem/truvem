<p align="center">
  <img src="https://raw.githubusercontent.com/truvem/truvem/main/logo.svg" alt="Truvem" width="150" height="150">
</p>

# Truvem

<p align="center">
  <img src="https://img.shields.io/pypi/v/truvem?style=for-the-badge&color=7c3aed" alt="PyPI version">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/Status-Beta-warning?style=for-the-badge" alt="Status: Beta">
  <img src="https://img.shields.io/badge/Proof-SHA--256-7c3aed?style=for-the-badge" alt="SHA-256">
</p>

<p align="center">
  <b>The proof layer for every AI action.</b><br>
  <i>Logged. Authorized. Verifiable.</i>
</p>

---

## 🧠 What is Truvem?

Truvem is **two things in one**:

### 1. Persistent Memory for AI Agents
Give your agent memory across sessions, models, and devices. Two API calls. Any model. Free.

### 2. The Proof Layer for Every AI Action
Every action your AI takes — logged with SHA-256, stored in an append-only ledger, verifiable forever.

> Like SSL/TLS for the web — invisible, but everything depends on it.

---

## 🤯 The Problem

**AI agents forget everything. And when they act, there's no proof.**

- Agents are stateless → no memory between sessions
- Agent actions are unverifiable → no tamper-evident audit trail
- Existing logs are mutable → useless for compliance or debugging

## 💡 The Solution

**Truvem = Memory + Proof. 2 lines of code. Any model.**

---

## 🚀 Quick Start

### Install

```bash
pip install truvem
```

### Memory (remember across sessions)

```python
from truvem import Truvem

client = Truvem(api_key="your_key")

# Store a memory
client.remember("agent-1", "User prefers dark mode")

# Recall — any session, any model
memories = client.recall("agent-1")
```

### Proof (cryptographic receipt for every action)

```python
# Log an action with immutable proof
response = client.log_action(
    agent_id="agent-1",
    model="gpt-4o",
    authorized_by="user@company.com",
    prompt="Send refund email",
    result="Email sent to user@example.com"
)

print(response["action_id"])   # da4c5ad4-...
print(response["proof_hash"])  # 872e4e50-... (SHA-256)

# Verify integrity at any time
proof = client.get_proof(response["action_id"])
```

---

## ⚡ API Endpoints

| Endpoint | Method | Description |
|:---|:---|:---|
| `/v1/register` | `POST` | Get your API key |
| `/v1/memory/write` | `POST` | Write a memory |
| `/v1/memory/read` | `POST` | Read memories |
| `/v1/memory/forget` | `DELETE` | Delete a memory |
| `/v1/memory/search` | `POST` | Search memories |
| `/v1/action/log` | `POST` | Log action + SHA-256 proof ✨ |
| `/v1/action/proof/{id}` | `GET` | Get verifiable proof ✨ |

---

## 🔒 Why "Proof Layer"?

| Feature | Traditional Logs | Truvem |
|:---|:---|:---|
| Tamper-evident | ❌ | ✅ SHA-256 |
| Append-only | ❌ | ✅ No UPDATE/DELETE |
| Verifiable | ❌ | ✅ Anyone can verify |
| 2 lines to add | ❌ | ✅ |
| Open standard | ❌ | ✅ TMX |

---

## 🤖 Supported Models

* 🟢 **GPT-4 / OpenAI**
* 🟣 **Claude / Anthropic**
* 🔵 **Gemini / Google**
* 🟠 **Mistral AI**
* 🦙 **Llama / Meta**
* ⚡ **Any model via REST API**

---

## 📦 Examples

→ [Proof-Your-Agent](./examples/proof-your-agent/) — Add cryptographic proof to your LangChain agent in 2 lines

---

## 🔗 TMX Protocol

Truvem is built on **TMX (Truvem Memory eXchange)** — an open standard for AI agent memory and action portability.

→ [Read the TMX spec](./TMX.md)
→ [Article on Dev.to](https://dev.to/truvem/tmx-the-open-standard-ai-agent-memory-has-been-waiting-for)

---

## 🔗 Links

* 🌐 **Website**: [truvem.github.io/truvem](https://truvem.github.io/truvem)
* 📚 **Live API & Docs**: [truvem.onrender.com/docs](https://truvem.onrender.com/docs)
* 🐙 **GitHub**: [github.com/truvem/truvem](https://github.com/truvem/truvem)
* 📦 **PyPI**: [pypi.org/project/truvem](https://pypi.org/project/truvem/)
* 🐦 **Twitter**: [@gettruvem](https://twitter.com/gettruvem)

---

<p align="center">
  <a href="https://truvem.github.io/truvem">
    <img src="https://raw.githubusercontent.com/truvem/truvem/main/badge-1.svg" alt="Powered by Truvem" height="28">
  </a>
</p>

<p align="center">
  <b>Built by Dieng Amine</b> • <a href="mailto:gettruvem@gmail.com">gettruvem@gmail.com</a>
</p>
