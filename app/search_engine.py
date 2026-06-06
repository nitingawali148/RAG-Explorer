"""BM25 keyword search over the pre-chunked corpus."""
from __future__ import annotations

from rank_bm25 import BM25Okapi

from .corpus import CHUNKS

_tokenize = lambda t: t.lower().split()

_bm25 = BM25Okapi([_tokenize(c["text"]) for c in CHUNKS])


def search(query: str, top_k: int = 4) -> list[dict]:
    scores = _bm25.get_scores(_tokenize(query))
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
    results = []
    for idx, score in ranked:
        if score > 1.0:
            chunk = CHUNKS[idx].copy()
            chunk["score"] = round(float(score), 4)
            results.append(chunk)
    return results
