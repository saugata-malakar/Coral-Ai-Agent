"""
Embedding, ChromaDB + BM25 loading, hybrid search (RRF).
Gracefully degrades to text-only search if GCP credentials or indexes are unavailable.
"""
import json
import logging
import pickle
import re

import numpy as np

from .config import (
    CHROMA_COLLECTION,
    CHROMA_DIR,
    BM25_FILE,
    BM25_MAP_FILE,
    CHUNKS_FILE,
    GCP_LOCATION,
    GCP_PROJECT,
    GEMINI_EMBED_MODEL,
    SA_KEY_DICT,
    DATA_DIR,
)

logger = logging.getLogger(__name__)

# ── Load chunks (always available) ────────────────────────────────────────────
_all_chunks = []
chunks_by_id = {}
if CHUNKS_FILE.exists():
    try:
        with open(CHUNKS_FILE, encoding="utf-8") as f:
            _all_chunks = json.load(f)
        chunks_by_id = {c["id"]: c for c in _all_chunks}
        logger.info(f"Loaded {len(_all_chunks)} chunks from {CHUNKS_FILE}")
    except Exception as e:
        logger.warning(f"Failed to load chunks: {e}")

# ── Vertex AI init (optional — may not have credentials) ─────────────────────
gcp_creds = None
_embed_model = None
_HAS_GCP = False

if SA_KEY_DICT:
    try:
        from google.oauth2 import service_account
        import vertexai
        from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

        gcp_creds = service_account.Credentials.from_service_account_info(
            SA_KEY_DICT, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        vertexai.init(project=GCP_PROJECT, location=GCP_LOCATION, credentials=gcp_creds)
        _embed_model = TextEmbeddingModel.from_pretrained(GEMINI_EMBED_MODEL)
        _HAS_GCP = True
        logger.info("GCP Vertex AI initialized successfully")
    except Exception as e:
        logger.warning(f"GCP credentials not available — running without embeddings: {e}")
else:
    logger.info("No GCP credentials configured — running in text-search-only mode")


def embed_query(text: str) -> list:
    """Embed a query using Vertex AI. Returns empty list if unavailable."""
    if not _HAS_GCP or _embed_model is None:
        return []
    try:
        from vertexai.language_models import TextEmbeddingInput
        result = _embed_model.get_embeddings(
            [TextEmbeddingInput(text=text, task_type="RETRIEVAL_QUERY")]
        )
        return result[0].values
    except Exception as e:
        logger.warning(f"Embedding failed: {e}")
        return []


# ── NLTK (optional) ───────────────────────────────────────────────────────────
_HAS_NLTK = False
try:
    import nltk
    nltk.download("punkt",     quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    _HAS_NLTK = True
except Exception as e:
    logger.warning(f"NLTK not available: {e}")


# ── ChromaDB (optional) ──────────────────────────────────────────────────────
collection = None
_HAS_CHROMA = False

if CHROMA_DIR.exists():
    try:
        import chromadb
        _chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        try:
            collection = _chroma_client.get_collection(CHROMA_COLLECTION)
        except Exception:
            collection = _chroma_client.get_collection("coastal_chunks_v2")
        _HAS_CHROMA = True
        logger.info(f"ChromaDB loaded: {collection.name} ({collection.count()} docs)")
    except Exception as e:
        logger.warning(f"ChromaDB not available: {e}")
else:
    logger.info("ChromaDB directory not found — will use text search only")


# ── BM25 (optional) ──────────────────────────────────────────────────────────
bm25 = None
bm25_mapping = []
_HAS_BM25 = False

if BM25_FILE.exists() and BM25_MAP_FILE.exists():
    try:
        with open(BM25_FILE, "rb") as f:
            bm25 = pickle.load(f)
        with open(BM25_MAP_FILE, encoding="utf-8") as f:
            bm25_mapping = json.load(f)
        _HAS_BM25 = True
        logger.info(f"BM25 index loaded ({len(bm25_mapping)} docs)")
    except Exception as e:
        logger.warning(f"BM25 index not available: {e}")
else:
    # Try to build BM25 from chunks
    if _all_chunks:
        try:
            from .build_indexes import build_bm25_index
            bm25, bm25_mapping = build_bm25_index(_all_chunks, DATA_DIR)
            _HAS_BM25 = True
            logger.info("BM25 index built from chunks.json")
        except Exception as e:
            logger.warning(f"Could not build BM25 index: {e}")


# ── Tokeniser ─────────────────────────────────────────────────────────────────
_DOMAIN_KEEP = {
    "wave","water","depth","period","height","force",
    "current","flow","pressure","energy","velocity","slope",
}

if _HAS_NLTK:
    _stemmer    = PorterStemmer()
    _stop_words = set(stopwords.words("english"))

def tokenize_bm25(text: str) -> list:
    if _HAS_NLTK:
        tokens = word_tokenize(text.lower())
        return [
            _stemmer.stem(t) for t in tokens
            if t.isalpha() and (t not in _stop_words or t in _DOMAIN_KEEP)
        ]
    else:
        # Simple fallback tokenizer
        return [w.lower() for w in re.split(r'\W+', text) if len(w) > 2]


# ── Fallback text search ─────────────────────────────────────────────────────
def _text_search(query: str, k: int = 8) -> list:
    """Simple keyword-based search as fallback when no indexes are available."""
    query_words = set(query.lower().split())
    scored = []
    for chunk in _all_chunks:
        text = chunk.get("text", "").lower()
        # Score by number of query words found in text
        score = sum(1 for w in query_words if w in text)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        {
            "id":       c["id"],
            "text":     c.get("text", ""),
            "metadata": c.get("metadata", {}),
            "rrf_score": s / max(1, len(query_words)),
        }
        for s, c in scored[:k]
    ]


# ── Hybrid search (RRF) ───────────────────────────────────────────────────────
def hybrid_search(query: str, k: int = 8) -> list:
    """
    Hybrid search combining dense (ChromaDB) + sparse (BM25) with RRF.
    Falls back to text search if indexes aren't available.
    """
    # If neither index is available, fall back to simple text search
    if not _HAS_BM25 and not _HAS_CHROMA:
        return _text_search(query, k)

    RRF_K, TOP_N = 60, 20

    dense_ranks = {}
    sparse_ranks = {}

    # Dense search via ChromaDB
    if _HAS_CHROMA and _HAS_GCP:
        try:
            q_vec = embed_query(query)
            if q_vec:
                chroma_res  = collection.query(query_embeddings=[q_vec], n_results=TOP_N)
                dense_ids   = chroma_res["ids"][0]
                dense_ranks = {cid: rank for rank, cid in enumerate(dense_ids)}
        except Exception as e:
            logger.warning(f"Dense search failed: {e}")

    # Sparse search via BM25
    if _HAS_BM25:
        try:
            bm25_scores   = bm25.get_scores(tokenize_bm25(query))
            bm25_top_idx  = np.argsort(bm25_scores)[::-1][:TOP_N]
            sparse_ranks  = {bm25_mapping[i]: rank for rank, i in enumerate(bm25_top_idx)}
        except Exception as e:
            logger.warning(f"Sparse search failed: {e}")

    # If both failed, fall back
    if not dense_ranks and not sparse_ranks:
        return _text_search(query, k)

    all_ids    = set(dense_ranks) | set(sparse_ranks)
    rrf_scores = {}
    for cid in all_ids:
        score = 0.0
        if cid in dense_ranks:
            score += 1.0 / (RRF_K + dense_ranks[cid])
        if cid in sparse_ranks:
            score += 1.0 / (RRF_K + sparse_ranks[cid])
        rrf_scores[cid] = score

    top_ids = sorted(rrf_scores, key=rrf_scores.get, reverse=True)[:k]
    return [
        {
            "id":       cid,
            "text":     chunks_by_id.get(cid, {}).get("text", ""),
            "metadata": chunks_by_id.get(cid, {}).get("metadata", {}),
            "rrf_score": rrf_scores[cid],
        }
        for cid in top_ids
    ]
