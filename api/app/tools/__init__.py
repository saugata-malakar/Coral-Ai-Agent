import logging

logger = logging.getLogger(__name__)

from .rag import rag_search
from .code_runner import run_python
from .latex import latex_generator
from .plotter import generate_plot
from .document_reader import read_document
from .thinking_modes import create_thinking_mode_tool
from .image_generator import create_visualization_tool, create_flowchart_tool
from .user_profile import create_user_profile_tool
from .resource_tracker import ResourceTracker

# Safe import of extract functions
try:
    from .resource_tracker import extract_sources_from_retrieval
except ImportError:
    def extract_sources_from_retrieval(*a, **kw):
        return []

# Core tools (always available)
ALL_TOOLS = [
    rag_search,
    run_python,
    latex_generator,
    generate_plot,
    read_document
]

# Enhanced tools (opt-in)
def get_enhanced_tools():
    """Get all tools including new enhancements."""
    tools = list(ALL_TOOLS)

    # Web search (optional — requires tavily)
    try:
        from .web_search import create_web_search_tool_definition
        web_search_tool = create_web_search_tool_definition()
        tools.append(web_search_tool)
    except Exception as e:
        logger.warning(f"Web search tool not available: {e}")

    try:
        thinking_mode_tool = create_thinking_mode_tool()
        tools.append(thinking_mode_tool)
    except Exception as e:
        logger.warning(f"Thinking mode tool not available: {e}")

    try:
        viz_tool = create_visualization_tool()
        flowchart_tool = create_flowchart_tool()
        tools.extend([viz_tool, flowchart_tool])
    except Exception as e:
        logger.warning(f"Visualization tools not available: {e}")

    try:
        profile_tool = create_user_profile_tool()
        tools.append(profile_tool)
    except Exception as e:
        logger.warning(f"Profile tool not available: {e}")

    return tools
