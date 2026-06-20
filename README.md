# Truvem

Universal persistent memory for AI agents.

## What is Truvem?

Truvem gives AI agents persistent memory across sessions,
models, and platforms. Works with GPT, Claude, Gemini,
Mistral, Llama — any model.

## The problem

AI agents forget everything between sessions.
Their weights are frozen. They have no memory layer.
Every conversation starts from zero.

## The solution

Truvem is the memory infrastructure layer for AI agents:
- Persistent memory across sessions
- Semantic context retrieval
- Works with any LLM

## Live API

https://truvem.onrender.com/docs

## Install SDK

pip install truvem

## Quick start

from truvem import Truvem

client = Truvem(api_key="your_key")
client.remember("agent-1", "User prefers dark mode")
memories = client.recall("agent-1")
