"""
Build BM25 index from chunks.json.
Called automatically by retrieval.py if the index doesn't exist.
"""
import json
import logging
import pickle
import re
from pathlib import Path

logger = logging.getLogger(__name__)


def _simple_tokenize(text: str) -> list[str]:
    """Simple tokenizer for building BM25 without NLTK dependency."""
    try:
        import nltk
        from nltk.corpus import stopwords
        from nltk.stem import PorterStemmer
        from nltk.tokenize import word_tokenize

        _stemmer = PorterStemmer()
        _stop_words = set(stopwords.words("english"))
        _domain_keep = {
            "wave", "water", "depth", "period", "height", "force",
            "current", "flow", "pressure", "energy", "velocity", "slope",
        }
        tokens = word_tokenize(text.lower())
        return [
            _stemmer.stem(t) for t in tokens
            if t.isalpha() and (t not in _stop_words or t in _domain_keep)
        ]
    except Exception:
        # Fallback: simple whitespace + lowering
        return [w.lower() for w in re.split(r'\W+', text) if len(w) > 2]


def build_bm25_index(chunks: list[dict], data_dir: Path) -> tuple:
    """
    Build BM25 index and mapping from chunks list.

    Args:
        chunks: List of chunk dicts with 'id' and 'text' keys
        data_dir: Directory to save the index files

    Returns:
        (bm25_index, mapping_list) tuple
    """
    from rank_bm25 import BM25Okapi

    logger.info(f"Building BM25 index from {len(chunks)} chunks...")

    # Tokenize all chunks
    corpus = []
    mapping = []
    for chunk in chunks:
        text = chunk.get("text", "")
        if text.strip():
            tokens = _simple_tokenize(text)
            corpus.append(tokens)
            mapping.append(chunk["id"])

    # Build BM25
    bm25 = BM25Okapi(corpus)

    # Save to disk
    bm25_file = data_dir / "bm25_index.pkl"
    mapping_file = data_dir / "bm25_mapping.json"

    with open(bm25_file, "wb") as f:
        pickle.dump(bm25, f)

    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f)

    logger.info(f"BM25 index saved: {len(mapping)} documents indexed")
    return bm25, mapping
