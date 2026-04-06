from .rag import rag_search
from .code_runner import run_python
from .latex import latex_generator
from .plotter import generate_plot
from .document_reader import read_document
from .web_search import create_web_search_tool_definition
from .thinking_modes import create_thinking_mode_tool
from .image_generator import create_visualization_tool, create_flowchart_tool
from .user_profile import create_user_profile_tool
from .resource_tracker import ResourceTracker, extract_sources_from_retrieval, extract_sources_from_web_search

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
    web_search_tool = create_web_search_tool_definition()
    thinking_mode_tool = create_thinking_mode_tool()
    viz_tool = create_visualization_tool()
    flowchart_tool = create_flowchart_tool()
    profile_tool = create_user_profile_tool()
    
    return ALL_TOOLS + [
        web_search_tool,
        thinking_mode_tool,
        viz_tool,
        flowchart_tool,
        profile_tool
    ]

