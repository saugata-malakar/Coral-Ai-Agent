"""
Resource attribution and tracking system.
Maintains provenance of all answers and sources used.
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class ResourceCitation:
    """Citation of a resource used in an answer."""
    source_id: str
    source_title: str
    source_type: str  # 'document', 'web', 'computed'
    relevance_score: float
    page_or_section: Optional[str] = None
    url: Optional[str] = None
    snippet: Optional[str] = None


@dataclass
class Answer:
    """Complete answer with resource provenance."""
    answer_id: str
    timestamp: str
    question: str
    answer_text: str
    citations: list[ResourceCitation]
    thinking_mode: str
    user_id: Optional[str] = None


class ResourceTracker:
    """Track and manage resource citations."""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.answers_dir = data_dir / "answers_with_citations"
        self.answers_dir.mkdir(parents=True, exist_ok=True)
    
    def create_citation(
        self,
        source_id: str,
        source_title: str,
        source_type: str,
        relevance_score: float,
        page_or_section: Optional[str] = None,
        url: Optional[str] = None,
        snippet: Optional[str] = None
    ) -> ResourceCitation:
        """Create a resource citation."""
        return ResourceCitation(
            source_id=source_id,
            source_title=source_title,
            source_type=source_type,
            relevance_score=relevance_score,
            page_or_section=page_or_section,
            url=url,
            snippet=snippet
        )
    
    def format_citations(self, citations: list[ResourceCitation]) -> str:
        """
        Format citations for display in answer.
        
        Args:
            citations: List of ResourceCitation objects
            
        Returns:
            Formatted citation section
        """
        if not citations:
            return ""
        
        formatted = "\n\n---\n**📚 Sources & Resources:**\n\n"
        
        for i, citation in enumerate(citations, 1):
            formatted += f"{i}. **{citation.source_title}** "
            formatted += f"({citation.source_type})"
            
            if citation.page_or_section:
                formatted += f" - {citation.page_or_section}"
            
            formatted += f" [Relevance: {citation.relevance_score:.1%}]\n"
            
            if citation.url:
                formatted += f"   🔗 {citation.url}\n"
            
            if citation.snippet:
                formatted += f"   📝 \"{citation.snippet[:100]}...\"\n"
            
            formatted += "\n"
        
        return formatted
    
    def save_answer_with_citations(
        self,
        question: str,
        answer_text: str,
        citations: list[ResourceCitation],
        thinking_mode: str,
        user_id: Optional[str] = None,
        answer_id: Optional[str] = None
    ) -> str:
        """
        Save answer with complete citation record.
        
        Args:
            question: Original question
            answer_text: Answer content
            citations: List of citations
            thinking_mode: Thinking mode used
            user_id: User ID if available
            answer_id: Custom answer ID (generated if not provided)
            
        Returns:
            Answer ID
        """
        if not answer_id:
            answer_id = f"answer_{datetime.now().isoformat().replace(':', '-')}"
        
        answer = Answer(
            answer_id=answer_id,
            timestamp=datetime.now().isoformat(),
            question=question,
            answer_text=answer_text,
            citations=citations,
            thinking_mode=thinking_mode,
            user_id=user_id
        )
        
        # Save to disk
        path = self.answers_dir / f"{answer_id}.json"
        path.write_text(json.dumps(asdict(answer), default=str, indent=2))
        
        return answer_id
    
    def get_answer(self, answer_id: str) -> Optional[Answer]:
        """Retrieve answer with citations."""
        path = self.answers_dir / f"{answer_id}.json"
        if path.exists():
            data = json.loads(path.read_text())
            # Convert citation dicts back to ResourceCitation objects
            citations = [ResourceCitation(**c) for c in data.get("citations", [])]
            data["citations"] = citations
            return Answer(**data)
        return None


def extract_sources_from_retrieval(retrieval_results: list) -> list[ResourceCitation]:
    """
    Extract resource citations from RAG retrieval results.
    
    Args:
        retrieval_results: Results from ChromaDB/RAG search
        
    Returns:
        List of ResourceCitation objects
    """
    citations = []
    
    for i, result in enumerate(retrieval_results):
        metadata = result.get("metadata", {}) if isinstance(result, dict) else {}
        
        citation = ResourceCitation(
            source_id=str(i),
            source_title=metadata.get("source", "Course Material"),
            source_type="document",
            relevance_score=result.get("score", 0.5) if isinstance(result, dict) else 0.5,
            page_or_section=metadata.get("section", None),
            snippet=result.get("content", "")[:200] if isinstance(result, dict) else None
        )
        citations.append(citation)
    
    return citations


def extract_sources_from_web_search(search_results: list) -> list[ResourceCitation]:
    """
    Extract resource citations from web search results.
    
    Args:
        search_results: Results from web search
        
    Returns:
        List of ResourceCitation objects
    """
    citations = []
    
    for i, result in enumerate(search_results):
        if isinstance(result, dict):
            citation = ResourceCitation(
                source_id=f"web_{i}",
                source_title=result.get("title", "Web Source"),
                source_type="web",
                relevance_score=0.8,
                url=result.get("link", ""),
                snippet=result.get("snippet", "")[:200]
            )
            citations.append(citation)
    
    return citations
