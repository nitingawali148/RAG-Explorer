"""RAG answer generation using Groq."""
from __future__ import annotations

import os
from dataclasses import dataclass

from .search_engine import search

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("RAG_MODEL", "llama-3.1-8b-instant")

_SYSTEM = """You are ShopBot, the RAG-powered customer support assistant for ShopSphere.
Answer ONLY using the retrieved context below. If the context does not contain the answer,
say so and direct the customer to support@shopsphere.com. Be concise and cite the source
document name in square brackets, e.g. [shipping_policy.md]."""


def answer(message: str, top_k: int = 4, history: list | None = None):
    hits = search(message, top_k=top_k)
    context = "\n\n".join(
        f"[{h['source']}]\n{h['text']}" for h in hits
    ) if hits else "No relevant context found."
    sources = list(dict.fromkeys(h["source"] for h in hits))

    if not GROQ_API_KEY:
        return {
            "answer": f"[mock mode — set GROQ_API_KEY] Retrieved {len(hits)} chunks for: \"{message}\". Top source: {sources[0] if sources else 'none'}.",
            "sources": sources,
            "hits": hits,
            "mode": "mock",
            "model": "mock",
            "retrieval_context": [h["text"] for h in hits],
        }

    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        messages = [{"role": "system", "content": _SYSTEM + "\n\nCONTEXT:\n" + context}]
        for turn in (history or []):
            messages.append({"role": turn.get("role", "user"), "content": turn.get("content", "")})
        messages.append({"role": "user", "content": message})
        resp = client.chat.completions.create(model=GROQ_MODEL, messages=messages, max_tokens=400, temperature=0.2)
        reply = resp.choices[0].message.content
    except Exception as e:
        reply = f"[error] {type(e).__name__}: {str(e)[:200]}"

    return {
        "answer": reply,
        "sources": sources,
        "hits": hits,
        "mode": "live",
        "model": GROQ_MODEL,
        "retrieval_context": [h["text"] for h in hits],
    }
