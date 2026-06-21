<p align="center">
  <img src="https://raw.githubusercontent.com/truvem/truvem/main/logo.svg" alt="Truvem" width="150" height="150">
</p>

# Truvem

<p align="center">
  <img src="https://img.shields.io/pypi/v/truvem?style=for-the-badge&color=6366f1" alt="PyPI version">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/Status-Beta-warning?style=for-the-badge" alt="Status: Beta">
</p>

> **Universal persistent memory for AI agents. Two API calls. Any model. Persistent.**

---

## 🤯 The Problem

**AI agents forget everything between sessions.** Whether you are building an autonomous researcher, a customer support bot, or a personal assistant, modern LLMs are fundamentally stateless. Existing solutions require complex vector databases, embedding pipelines, and custom retrieval logic just to remember basic user preferences.

## 💡 The Solution

**Truvem = 2 API calls, any model, persistent.** Dead-simple memory infrastructure for AI agents. Give your agent infinite context without the infrastructure headache.

---

## 🚀 Quick Start

### 1. Installation

```bash
pip install truvem
```

### 2. Usage

```python
from truvem import Truvem

client = Truvem(api_key="your_key")

# Store a memory
client.remember("agent-1", "User prefers dark mode")

# Recall memories
memories = client.recall("agent-1")
print(memories)
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

---

## 🤖 Supported Models

* 🟢 **GPT-4 / OpenAI**
* 🟣 **Claude / Anthropic**
* 🔵 **Gemini / Google**
* 🟠 **Mistral AI**
* 🦙 **Llama / Meta**

---

## 🔗 Links

* 🌐 **Website**: [truvem.github.io/truvem](https://truvem.github.io/truvem)
* 📚 **Live API & Docs**: [truvem.onrender.com/docs](https://truvem.onrender.com/docs)
* 🐙 **GitHub**: [github.com/truvem/truvem](https://github.com/truvem/truvem)

---

<p align="center">
  <b>Made by Truvem</b> • <a href="mailto:gettruvem@gmail.com">gettruvem@gmail.com</a>
</p>
