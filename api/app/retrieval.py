"""
Embedding, ChromaDB + BM25 loading, hybrid search (RRF).
"""
import json
import pickle

import chromadb
import nltk
import numpy as np
import vertexai
from google.oauth2 import service_account
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

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
)

nltk.download("punkt",     quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

# ── Vertex AI init ────────────────────────────────────────────────────────────
gcp_creds = service_account.Credentials.from_service_account_info(
    SA_KEY_DICT, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
vertexai.init(project=GCP_PROJECT, location=GCP_LOCATION, credentials=gcp_creds)

# ── Embedding model ───────────────────────────────────────────────────────────
_embed_model = TextEmbeddingModel.from_pretrained(GEMINI_EMBED_MODEL)

def embed_query(text: str) -> list:
    result = _embed_model.get_embeddings(
        [TextEmbeddingInput(text=text, task_type="RETRIEVAL_QUERY")]
    )
    return result[0].values

# ── ChromaDB ──────────────────────────────────────────────────────────────────
_chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
try:
    collection = _chroma_client.get_collection(CHROMA_COLLECTION)
except Exception:
    collection = _chroma_client.get_collection("coastal_chunks_v2")

# ── BM25 ──────────────────────────────────────────────────────────────────────
with open(BM25_FILE, "rb") as f:
    bm25 = pickle.load(f)
with open(BM25_MAP_FILE, encoding="utf-8") as f:
    bm25_mapping = json.load(f)
with open(CHUNKS_FILE, encoding="utf-8") as f:
    _all_chunks = json.load(f)
chunks_by_id = {c["id"]: c for c in _all_chunks}

# ── Tokeniser ─────────────────────────────────────────────────────────────────
_DOMAIN_KEEP = {
    "wave","water","depth","period","height","force",
    "current","flow","pressure","energy","velocity","slope",
}
_stemmer    = PorterStemmer()
_stop_words = set(stopwords.words("english"))

def tokenize_bm25(text: str) -> list:
    tokens = word_tokenize(text.lower())
    return [
        _stemmer.stem(t) for t in tokens
        if t.isalpha() and (t not in _stop_words or t in _DOMAIN_KEEP)
    ]

# ── Hybrid search (RRF) ───────────────────────────────────────────────────────
def hybrid_search(query: str, k: int = 8) -> list:
    RRF_K, TOP_N = 60, 20

    q_vec = embed_query(query)
    chroma_res  = collection.query(query_embeddings=[q_vec], n_results=TOP_N)
    dense_ids   = chroma_res["ids"][0]
    dense_ranks = {cid: rank for rank, cid in enumerate(dense_ids)}

    bm25_scores   = bm25.get_scores(tokenize_bm25(query))
    bm25_top_idx  = np.argsort(bm25_scores)[::-1][:TOP_N]
    sparse_ranks  = {bm25_mapping[i]: rank for rank, i in enumerate(bm25_top_idx)}

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
