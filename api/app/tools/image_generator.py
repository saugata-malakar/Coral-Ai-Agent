"""
Image generation for diagrams, flowcharts, and visualizations.
Supports ASCII art, SVG, and matplotlib-based generation.
"""
import io
from pathlib import Path
from typing import Optional


def create_flowchart_tool():
    """Create tool for generating flowcharts using Graphviz."""
    from langchain_core.tools import tool
    
    @tool
    def generate_flowchart(
        description: str,
        diagram_format: str = "mermaid"
    ) -> str:
        """
        Generate a flowchart or diagram from a description.
        
        Args:
            description: Description of the flowchart structure
            diagram_format: Format - 'mermaid', 'graphviz', or 'ascii'
            
        Returns:
            Diagram code/markup or path to generated image
        """
        if diagram_format == "mermaid":
            return f"```mermaid\n{description}\n```"
        elif diagram_format == "graphviz":
            try:
                import graphviz
                # Generate DOT format diagram
                return f"Graphviz diagram:\n{description}"
            except ImportError:
                return "Graphviz not available"
        else:
            return description
    
    return generate_flowchart


def create_diagram_ascii(title: str, content: list[str]) -> str:
    """Create ASCII art diagram."""
    width = max(len(line) for line in content) + 4
    border = "┌" + "─" * (width - 2) + "┐"
    lines = [border, f"│ {title:<{width-4}} │"]
    lines.append("├" + "─" * (width - 2) + "┤")
    
    for line in content:
        lines.append(f"│ {line:<{width-4}} │")
    
    lines.append("└" + "─" * (width - 2) + "┘")
    return "\n".join(lines)


def create_process_diagram(steps: list[str]) -> str:
    """
    Create a process flow diagram using ASCII art.
    
    Args:
        steps: List of process steps
        
    Returns:
        ASCII art diagram
    """
    result = []
    for i, step in enumerate(steps):
        result.append(f"Step {i+1}: {step}")
        if i < len(steps) - 1:
            result.append("    ↓")
    return "\n".join(result)


def create_concept_diagram(title: str, concepts: dict[str, list[str]]) -> str:
    """
    Create a concept relationship diagram.
    
    Args:
        title: Diagram title
        concepts: Dict mapping concept names to attributes
        
    Returns:
        ASCII art concept diagram
    """
    lines = [f"\n{'='*50}"]
    lines.append(f"CONCEPT: {title}")
    lines.append('='*50)
    
    for concept, attributes in concepts.items():
        lines.append(f"\n◆ {concept}")
        for attr in attributes:
            lines.append(f"  → {attr}")
    
    return "\n".join(lines)


def create_hierarchy_diagram(root: str, children: dict) -> str:
    """
    Create hierarchical structure diagram.
    
    Args:
        root: Root node name
        children: Nested dict of child nodes
        
    Returns:
        ASCII hierarchy diagram
    """
    def build_tree(name: str, nodes: dict, prefix: str = "") -> list[str]:
        lines = [prefix + "├─ " + name]
        if isinstance(nodes, dict):
            items = list(nodes.items())
            for i, (key, value) in enumerate(items):
                is_last = i == len(items) - 1
                next_prefix = prefix + ("   " if is_last else "│  ")
                lines.extend(build_tree(key, value, next_prefix))
        return lines
    
    lines = [root]
    lines.extend(build_tree(root, children, ""))
    return "\n".join(lines)


def create_comparison_table(title: str, rows: list[dict]) -> str:
    """
    Create ASCII table for comparisons.
    
    Args:
        title: Table title
        rows: List of dicts with row data
        
    Returns:
        Formatted ASCII table
    """
    if not rows:
        return title
    
    # Get all keys from first row
    keys = list(rows[0].keys())
    
    # Calculate column widths
    widths = {key: len(str(key)) for key in keys}
    for row in rows:
        for key in keys:
            widths[key] = max(widths[key], len(str(row.get(key, ""))))
    
    # Build table
    lines = [title]
    lines.append("=" * sum(widths.values()) + len(keys) * 3)
    
    # Header
    header = " | ".join(f"{key:^{widths[key]}}" for key in keys)
    lines.append(header)
    lines.append("-" * sum(widths.values()) + len(keys) * 3)
    
    # Rows
    for row in rows:
        row_str = " | ".join(f"{str(row.get(k, '')):<{widths[k]}}" for k in keys)
        lines.append(row_str)
    
    return "\n".join(lines)


def create_visualization_tool():
    """Create tool for generating various visualizations."""
    from langchain_core.tools import tool
    
    @tool
    def generate_diagram(
        diagram_type: str,
        data: dict
    ) -> str:
        """
        Generate various types of diagrams.
        
        Supported types:
        - process: Process flow diagram
        - concept: Concept relationship map
        - hierarchy: Hierarchical structure
        - comparison: Comparison table
        - flowchart: Process flowchart
        
        Args:
            diagram_type: Type of diagram to generate
            data: Dict containing diagram specifications
            
        Returns:
            Generated diagram as ASCII art or code
        """
        diagram_type = diagram_type.lower()
        
        if diagram_type == "process":
            steps = data.get("steps", [])
            return create_process_diagram(steps)
        
        elif diagram_type == "concept":
            title = data.get("title", "Concept Map")
            concepts = data.get("concepts", {})
            return create_concept_diagram(title, concepts)
        
        elif diagram_type == "hierarchy":
            root = data.get("root", "Root")
            children = data.get("children", {})
            return create_hierarchy_diagram(root, children)
        
        elif diagram_type == "comparison":
            title = data.get("title", "Comparison")
            rows = data.get("rows", [])
            return create_comparison_table(title, rows)
        
        else:
            return f"Unsupported diagram type: {diagram_type}"
    
    return generate_diagram
