"""
FastAPI route definitions.
"""
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel

from .agent import run_agent
from .config import PLOTS_DIR, UPLOADS_DIR, DATA_DIR
from .retrieval import collection
from .tools.latex import compile_latex
from .tools.user_profile import UserProfileManager
from .tools.resource_tracker import ResourceTracker
from .tools.thinking_modes import ThinkingMode

router = APIRouter()

PLOT_TTL_SECONDS = 2 * 60 * 60  # 2 hours
CONVERSATIONS_FILE = DATA_DIR / "conversations.json"

# Initialize managers
user_profile_manager = UserProfileManager(DATA_DIR)
resource_tracker = ResourceTracker(DATA_DIR)


def cleanup_old_plots():
    """Delete plots older than PLOT_TTL_SECONDS. Called on server startup."""
    now = time.time()
    for f in PLOTS_DIR.glob("*.png"):
        if now - f.stat().st_mtime > PLOT_TTL_SECONDS:
            f.unlink(missing_ok=True)


# ── Conversation metadata store ───────────────────────────────────────────────

class Conversation(BaseModel):
    id: str
    title: str
    created_at: str
    updated_at: str
    message_count: int = 0


conversations_store: dict[str, Conversation] = {}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _save_conversations() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CONVERSATIONS_FILE.write_text(
        json.dumps({k: v.model_dump() for k, v in conversations_store.items()}, indent=2),
        encoding="utf-8",
    )


def _load_conversations() -> None:
    if CONVERSATIONS_FILE.exists():
        try:
            data = json.loads(CONVERSATIONS_FILE.read_text(encoding="utf-8"))
            for k, v in data.items():
                conversations_store[k] = Conversation(**v)
        except Exception as exc:
            print(f"[conversations] Failed to load {CONVERSATIONS_FILE}: {exc}")


# Load persisted conversations on module import
_load_conversations()


# ── Request / response models ─────────────────────────────────────────────────

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None  # auto-generated if omitted
    user_id: Optional[str] = None  # for personalization
    thinking_mode: Optional[str] = "standard"  # NEW: standard, deep, critical, analytical, comprehensive
    enable_web_search: Optional[bool] = False  # NEW: enable web search
    enable_resource_citations: Optional[bool] = True  # NEW: include source citations


class ChatResponse(BaseModel):
    text: str
    plots: list[str]
    session_id: str


class LatexRequest(BaseModel):
    latex: str


class ConversationCreate(BaseModel):
    id: Optional[str] = None
    title: str = "New Chat"


class ConversationPatch(BaseModel):
    title: str


# ── Endpoints ─────────────────────────────────────────────────────────────────

@router.get("/health")
def health():
    return {
        "status": "ok",
        "collection": collection.name if collection else "unavailable",
        "chunks": collection.count() if collection else 0,
    }


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """Plain text chat. Creates a new session if session_id is not provided."""
    session_id = req.session_id or uuid.uuid4().hex
    try:
        result = run_agent(
            req.message,
            session_id=session_id,
            user_id=req.user_id,
            thinking_mode=req.thinking_mode or "standard",
            enable_web_search=req.enable_web_search or False,
            enable_resource_citations=req.enable_resource_citations if req.enable_resource_citations is not None else True
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    
    plot_urls = ["/plots/" + Path(p).name for p in result["plots"]]

    # Update message count if conversation is tracked
    if session_id in conversations_store:
        conv = conversations_store[session_id]
        conversations_store[session_id] = conv.model_copy(
            update={"message_count": conv.message_count + 1, "updated_at": _now_iso()}
        )
        _save_conversations()

    return ChatResponse(text=result["text"], plots=plot_urls, session_id=session_id)


@router.post("/chat-with-file", response_model=ChatResponse)
async def chat_with_file(
    message: str = Form(...),
    file: UploadFile = File(...),
    session_id: Optional[str] = Form(None),
    user_id: Optional[str] = Form(None),
    thinking_mode: Optional[str] = Form("standard"),
    enable_web_search: Optional[bool] = Form(False),
):
    """Chat with an attached PDF or image (jpg/png/jpeg)."""
    ext = Path(file.filename).suffix.lower()
    if ext not in (".pdf", ".png", ".jpg", ".jpeg"):
        raise HTTPException(status_code=400, detail="Only PDF/PNG/JPG supported.")

    sid = session_id or uuid.uuid4().hex
    save_path = UPLOADS_DIR / f"{uuid.uuid4().hex}{ext}"
    save_path.write_bytes(await file.read())

    query = f"{message}\n\nFile available at: {save_path}"
    try:
        result = run_agent(
            query,
            session_id=sid,
            user_id=user_id,
            thinking_mode=thinking_mode or "standard",
            enable_web_search=enable_web_search or False,
            enable_resource_citations=True
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    
    plot_urls = ["/plots/" + Path(p).name for p in result["plots"]]

    if sid in conversations_store:
        conv = conversations_store[sid]
        conversations_store[sid] = conv.model_copy(
            update={"message_count": conv.message_count + 1, "updated_at": _now_iso()}
        )
        _save_conversations()

    return ChatResponse(text=result["text"], plots=plot_urls, session_id=sid)


@router.get("/plots/{filename}")
def get_plot(filename: str):
    """Fetch a generated plot image by filename."""
    path = PLOTS_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Plot not found.")
    return FileResponse(str(path), media_type="image/png")


@router.delete("/plots/{filename}")
def delete_plot(filename: str):
    """Delete a plot after the user has downloaded or dismissed it."""
    path = PLOTS_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail="Plot not found.")
    path.unlink()
    return {"deleted": True, "filename": filename}


@router.post("/compile-latex")
def compile_latex_endpoint(req: LatexRequest):
    """
    Compile LaTeX source to PDF.
    Auto-selects pdflatex or xelatex based on detected packages; falls back to the other.
    Returns PDF binary on success, or JSON error with details.
    """
    pdf_bytes, error_msg = compile_latex(req.latex)
    if pdf_bytes is None:
        raise HTTPException(
            status_code=422,
            detail={
                "error": "LaTeX compilation failed.",
                "fallback": error_msg or "Download the .tex file and compile locally.",
            },
        )
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=document.pdf"},
    )


# ── Conversation management endpoints ────────────────────────────────────────

@router.get("/conversations")
def list_conversations() -> list[Conversation]:
    """Return all conversations sorted newest-first."""
    return sorted(
        conversations_store.values(),
        key=lambda c: c.updated_at,
        reverse=True,
    )


@router.post("/conversations", response_model=Conversation)
def create_conversation(body: ConversationCreate) -> Conversation:
    """Create (or upsert) a conversation entry."""
    conv_id = body.id or uuid.uuid4().hex
    now = _now_iso()
    conv = Conversation(
        id=conv_id,
        title=body.title,
        created_at=now,
        updated_at=now,
        message_count=0,
    )
    conversations_store[conv_id] = conv
    _save_conversations()
    return conv


@router.patch("/conversations/{conv_id}", response_model=Conversation)
def update_conversation(conv_id: str, body: ConversationPatch) -> Conversation:
    """Update the title of a conversation."""
    if conv_id not in conversations_store:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    conv = conversations_store[conv_id]
    conversations_store[conv_id] = conv.model_copy(
        update={"title": body.title, "updated_at": _now_iso()}
    )
    _save_conversations()
    return conversations_store[conv_id]


@router.delete("/conversations/{conv_id}")
def delete_conversation(conv_id: str):
    """Delete a conversation entry."""
    if conv_id not in conversations_store:
        raise HTTPException(status_code=404, detail="Conversation not found.")
    del conversations_store[conv_id]
    _save_conversations()
    return {"deleted": True, "id": conv_id}


# ── NEW ENHANCEMENT ENDPOINTS ─────────────────────────────────────────────────

@router.get("/user/{user_id}/profile")
def get_user_profile(user_id: str):
    """Get user learning profile and statistics."""
    profile = user_profile_manager.get_profile(user_id)
    stats = user_profile_manager.get_learning_stats(user_id)
    return {
        "profile": profile.__dict__,
        "statistics": stats
    }


@router.patch("/user/{user_id}/profile")
def update_user_profile(
    user_id: str,
    expertise_level: Optional[str] = None,
    preferred_format: Optional[str] = None,
    preferred_thinking_mode: Optional[str] = None
):
    """Update user profile preferences."""
    profile = user_profile_manager.get_profile(user_id)
    
    if expertise_level:
        profile.expertise_level = expertise_level
    if preferred_format:
        profile.preferred_format = preferred_format
    if preferred_thinking_mode:
        profile.preferred_thinking_mode = preferred_thinking_mode
    
    user_profile_manager.save_profile(profile)
    
    return {
        "message": "Profile updated",
        "profile": profile.__dict__
    }


@router.get("/user/{user_id}/history")
def get_user_history(user_id: str, limit: int = 10):
    """Get user interaction history."""
    history = user_profile_manager.get_interaction_history(user_id, limit=limit)
    return {"user_id": user_id, "interactions": history}


@router.get("/thinking-modes")
def list_thinking_modes():
    """List available thinking modes."""
    return {
        "available_modes": [
            {
                "id": "standard",
                "name": "Standard",
                "description": "Normal reasoning - balanced and efficient"
            },
            {
                "id": "deep",
                "name": "Deep Thinking",
                "description": "Extended analysis and exploration of the problem"
            },
            {
                "id": "critical",
                "name": "Critical Analysis",
                "description": "Questioning assumptions and validating conclusions"
            },
            {
                "id": "analytical",
                "name": "Mathematical Rigor",
                "description": "Step-by-step mathematical analysis with verification"
            },
            {
                "id": "comprehensive",
                "name": "Comprehensive",
                "description": "Multi-disciplinary synthesis and broad perspective"
            }
        ]
    }


@router.post("/answer/{answer_id}")
def get_answer_with_citations(answer_id: str):
    """Retrieve a previous answer with all citations."""
    answer = resource_tracker.get_answer(answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    return {
        "question": answer.question,
        "answer": answer.answer_text,
        "citations": [
            {
                "title": c.source_title,
                "type": c.source_type,
                "relevance": c.relevance_score,
                "page": c.page_or_section,
                "url": c.url
            }
            for c in answer.citations
        ],
        "thinking_mode": answer.thinking_mode,
        "timestamp": answer.timestamp
    }


@router.post("/rate-answer")
def rate_answer(
    answer_id: str,
    rating: int,
    feedback: Optional[str] = None,
    user_id: Optional[str] = None
):
    """Submit rating and feedback for an answer."""
    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    
    # Record in user interaction history
    if user_id:
        answer = resource_tracker.get_answer(answer_id)
        if answer:
            user_profile_manager.record_interaction(
                user_id=user_id,
                question=answer.question,
                thinking_mode=answer.thinking_mode,
                topic_tags=[],
                answer_length=len(answer.answer_text),
                rating=rating,
                feedback=feedback
            )
    
    return {
        "message": "Rating recorded",
        "answer_id": answer_id,
        "rating": rating
    }


@router.get("/diagrams/types")
def list_diagram_types():
    """List available diagram generation types."""
    return {
        "available_diagrams": [
            {
                "id": "process",
                "name": "Process Flow",
                "description": "Linear process or workflow diagram"
            },
            {
                "id": "concept",
                "name": "Concept Map",
                "description": "Interconnected concepts and relationships"
            },
            {
                "id": "hierarchy",
                "name": "Hierarchy",
                "description": "Hierarchical structure or taxonomy"
            },
            {
                "id": "comparison",
                "name": "Comparison Table",
                "description": "Side-by-side comparison"
            }
        ]
    }

