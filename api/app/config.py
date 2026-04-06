"""
Central config: credentials, model names, paths, constants.
All secrets loaded from api/.env — never hardcoded.
"""
import json
import os
import sys as _sys
from pathlib import Path

from dotenv import load_dotenv

# ── File paths ────────────────────────────────────────────────────────────────
PROJECT_ROOT  = Path(__file__).parent.parent   # /app in container, .../api locally
DATA_DIR      = PROJECT_ROOT / "data"
CHROMA_DIR    = DATA_DIR / "chroma"
BM25_FILE     = DATA_DIR / "bm25_index.pkl"
BM25_MAP_FILE = DATA_DIR / "bm25_mapping.json"
CHUNKS_FILE   = DATA_DIR / "chunks.json"
PLOTS_DIR     = PROJECT_ROOT / "plots"
UPLOADS_DIR   = PROJECT_ROOT / "uploads"

PLOTS_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

# ── Load .env ─────────────────────────────────────────────────────────────────
_env_path = PROJECT_ROOT / ".env"
if _env_path.exists():
    load_dotenv(_env_path)

# ── GCP credentials ───────────────────────────────────────────────────────────
_sa_key_path = os.getenv("GCP_SA_KEY_PATH", "")
SA_KEY_DICT = {}
GCP_PROJECT = "coastal-ai"  # Fallback value

if _sa_key_path:
    _api_dir = PROJECT_ROOT
    _sa_key_resolved = (_api_dir / _sa_key_path).resolve()
    if _sa_key_resolved.exists():
        with open(_sa_key_resolved, encoding="utf-8") as _f:
            SA_KEY_DICT = json.load(_f)
            GCP_PROJECT = SA_KEY_DICT.get("project_id", "coastal-ai")
    else:
        # In container, use env var if available
        GCP_PROJECT = os.getenv("GCP_PROJECT", "coastal-ai")
else:
    GCP_PROJECT = os.getenv("GCP_PROJECT", "coastal-ai")

GCP_LOCATION       = os.getenv("GCP_LOCATION", "us-central1")
GEMINI_MODEL       = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_EMBED_MODEL = os.getenv("GEMINI_EMBED_MODEL", "text-embedding-004")
CHROMA_COLLECTION  = os.getenv("CHROMA_COLLECTION", "coastal_chunks_v3")

# ── Python executable for subprocess code execution ───────────────────────────
_venv_python = PROJECT_ROOT / "venv" / "Scripts" / "python.exe"   # Windows
if not _venv_python.exists():
    _venv_python = PROJECT_ROOT / "venv" / "bin" / "python"        # Linux/Mac
SUBPROCESS_PYTHON = str(_venv_python) if _venv_python.exists() else _sys.executable
