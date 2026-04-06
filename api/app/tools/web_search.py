"""
Web search tool for real-time information retrieval.
Uses Tavily API for fast, reliable search results.
"""
import os
from typing import Optional
from langchain_community.tools.tavily_search import TavilySearchResults

def get_web_search_tool():
    """Initialize and return web search tool."""
    tavily_api_key = os.getenv("TAVILY_API_KEY", "")
    if not tavily_api_key:
        return None
    
    return TavilySearchResults(
        max_results=5,
        tavily_api_key=tavily_api_key,
        search_depth="advanced"  # More thorough search
    )


def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Perform web search and return results with sources.
    
    Args:
        query: Search query string
        max_results: Maximum number of results to return
        
    Returns:
        List of search results with title, link, and snippet
    """
    tool = get_web_search_tool()
    if not tool:
        return []
    
    try:
        results = tool.invoke({"query": query})
        # Convert to list if string
        if isinstance(results, str):
            import json
            results = json.loads(results)
        return results
    except Exception as e:
        print(f"Web search error: {e}")
        return []


def create_web_search_tool_definition():
    """Create LangChain tool definition for ReAct agent."""
    from langchain_core.tools import tool
    
    @tool
    def web_search(query: str) -> str:
        """
        Search the web for real-time information on coastal engineering topics.
        
        Args:
            query: Search query string
            
        Returns:
            Formatted search results with sources and citations
        """
        results = search_web(query)
        if not results:
            return "No web search results available or API not configured."
        
        formatted = "**Web Search Results:**\n\n"
        for i, result in enumerate(results, 1):
            if isinstance(result, dict):
                title = result.get("title", "No title")
                link = result.get("link", "No link")
                snippet = result.get("snippet", "")
                formatted += f"{i}. **{title}**\n"
                formatted += f"   Source: {link}\n"
                formatted += f"   {snippet}\n\n"
        
        return formatted
    
    return web_search
