import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .corpus import CHUNKS, STATS
from .search_engine import search
from .rag_chat import answer

HERE = Path(__file__).resolve().parent

app = FastAPI(title="ShopSphere RAG Explorer", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory=str(HERE / "static")), name="static")

templates = Jinja2Templates(directory=str(HERE / "templates"))

_EMBED_INFO = {"model": "BM25 (keyword)", "host": "in-memory"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "stats": STATS,
        "embed": _EMBED_INFO,
        "groq_configured": bool(os.getenv("GROQ_API_KEY")),
    })


@app.get("/ingest", response_class=HTMLResponse)
def ingest_page(request: Request):
    return templates.TemplateResponse("ingest.html", {
        "request": request,
        "stats": STATS,
        "available_files": list(set(c["source"] for c in CHUNKS)),
        "chunks": CHUNKS,
    })


@app.get("/search", response_class=HTMLResponse)
def search_page(request: Request, q: str = "", k: int = 4):
    hits = search(q, top_k=k) if q else []
    return templates.TemplateResponse("search.html", {
        "request": request,
        "q": q, "k": k,
        "hits": hits,
        "stats": STATS,
    })


@app.get("/chat", response_class=HTMLResponse)
def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "stats": STATS,
        "groq_configured": bool(os.getenv("GROQ_API_KEY")),
    })


@app.get("/api/health")
def health():
    return {"status": "ok", "stats": STATS, "embed": _EMBED_INFO, "groq_configured": bool(os.getenv("GROQ_API_KEY"))}


@app.get("/api/stats")
def api_stats():
    return STATS


@app.get("/api/chunks")
def api_chunks(source: str = None):
    data = [c for c in CHUNKS if not source or c["source"] == source]
    return {"chunks": data}


@app.post("/api/search")
async def api_search(request: Request):
    body = await request.json()
    hits = search(body.get("query", ""), top_k=int(body.get("top_k", 4)))
    return {"query": body.get("query"), "hits": hits}


@app.post("/api/chat")
async def api_chat(request: Request):
    body = await request.json()
    return answer(body.get("message", ""), top_k=int(body.get("top_k", 4)), history=body.get("history"))
