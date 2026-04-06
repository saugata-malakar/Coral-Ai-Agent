from langchain_core.tools import tool
from ..retrieval import hybrid_search


@tool
def rag_search(query: str) -> str:
    """Search the coastal hydrodynamics course materials (textbooks, lectures, tutorials).
    Always call this first for any course-related question before answering."""
    results = hybrid_search(query, k=8)
    texts = [r["text"] for r in results if r.get("text", "").strip()]
    if not texts:
        return "No relevant course materials found for this query."
    return "\n\n---\n\n".join(texts)
