"""
Thinking modes for deep reasoning and critical analysis.
Implements multiple reasoning strategies for complex problems.
"""
from enum import Enum
from typing import Optional


class ThinkingMode(str, Enum):
    """Different thinking modes available to the agent."""
    STANDARD = "standard"              # Normal reasoning
    DEEP = "deep"                       # Deep thinking with more steps
    CRITICAL = "critical"               # Critical analysis with counterargument
    ANALYTICAL = "analytical"           # Step-by-step mathematical analysis
    COMPREHENSIVE = "comprehensive"     # Multi-faceted approach
    MATHEMATICAL = "mathematical"       # Top-notch mathematical rigor


class ThinkingPrompts:
    """Prompts for different thinking modes."""
    
    DEEP_THINKING = """
    For this complex problem, perform DEEP THINKING by:
    
    1. **Break Down**: Decompose into fundamental sub-problems
    2. **Explore**: Consider multiple solution approaches
    3. **Verify**: Check each step independently
    4. **Synthesize**: Combine insights into comprehensive answer
    5. **Validate**: Cross-check final answer using different method
    
    Show your reasoning process explicitly at each step.
    """
    
    CRITICAL_THINKING = """
    For this problem, apply CRITICAL THINKING:
    
    1. **Question Assumptions**: What are we assuming? Are they valid?
    2. **Consider Limitations**: What are the constraints and boundaries?
    3. **Alternative Views**: What would a skeptic say? Consider counterarguments
    4. **Evidence Quality**: What's the quality of sources/evidence?
    5. **Implications**: What are broader implications and edge cases?
    6. **Conclusions**: What can we confidently conclude given the evidence?
    """
    
    ANALYTICAL_THINKING = """
    For this mathematical/computational problem, provide ANALYTICAL reasoning:
    
    1. **Mathematical Foundation**: State governing equations and relationships
    2. **Assumptions**: List all assumptions clearly
    3. **Solution Steps**: Walk through each step methodically with SymbolicCoastalMath tools
    4. **Intermediate Results**: Show and verify each intermediate result using run_python
    5. **Dimensional Analysis**: Verify units and dimensions throughout - check with COASTAL_CONSTANTS
    6. **Error Analysis**: Report absolute/relative errors and verification status
    7. **Sensitivity Analysis**: How sensitive is result to parameter changes?
    8. **Bounds Check**: Are results reasonable? Compare to known bounds and physical limits
    9. **Multiple Methods**: When possible, verify using alternative numerical approaches
    10. **Detailed Output**: Include all calculations with full precision and uncertainty bounds
    """
    
    COMPREHENSIVE = """
    For this problem, provide COMPREHENSIVE analysis:
    
    1. **Theoretical Framework**: What theories and principles apply?
    2. **Mathematical Foundation**: Show all governing equations with derivations
    3. **Historical Context**: How has this been approached before?
    4. **Multi-disciplinary**: Consider contributions from different fields
    5. **Numerical Computation**: Use SymbolicCoastalMath and advanced solvers
    6. **Verification Methods**: Cross-check using multiple approaches
    7. **Practical Implications**: Real-world applications and limitations
    8. **Uncertainty Quantification**: Report error bounds and confidence
    9. **Research State**: What do current publications say?
    10. **Synthesis**: Integrate all perspectives into unified, excellent answer
    """
    
    MATHEMATICAL_RIGOROUS = """
    For this problem, provide TOP-NOTCH MATHEMATICAL presentation:
    
    1. **Complete Derivation**: Every equation derived from first principles
    2. **Symbolic Computation**: Use sympy for symbolic verification
    3. **Numerical Accuracy**: All computations via run_python with brentq/fsolve
    4. **Verification Protocol**: Report verification status and error metrics
    5. **Dimensional Consistency**: Verify units at every step using COASTAL_CONSTANTS
    6. **Boundary Conditions**: Explicitly state and verify boundary conditions
    7. **Physical Limits**: Check limiting cases (e.g., kh → 0, kh → ∞)
    8. **Complete Output**: Show formula, substitution, result, units, and verification
    9. **Tabular Results**: For multi-case problems, use tables with all results
    10. **Final Answer**: Clearly highlighted with full context and uncertainty
    """


def get_thinking_mode_prompt(mode: str = "standard") -> str:
    """
    Get the system prompt enhancement for a thinking mode.
    
    Args:
        mode: Thinking mode name
        
    Returns:
        Prompt string to enhance reasoning
    """
    mode = mode.lower()
    
    if mode == ThinkingMode.DEEP:
        return ThinkingPrompts.DEEP_THINKING
    elif mode == ThinkingMode.CRITICAL:
        return ThinkingPrompts.CRITICAL_THINKING
    elif mode == ThinkingMode.ANALYTICAL:
        return ThinkingPrompts.ANALYTICAL_THINKING
    elif mode == ThinkingMode.COMPREHENSIVE:
        return ThinkingPrompts.COMPREHENSIVE
    elif mode == ThinkingMode.MATHEMATICAL or mode == "mathematical":
        return ThinkingPrompts.MATHEMATICAL_RIGOROUS
    else:
        return ""


def get_thinking_mode_system_prompt(selected_mode: str) -> str:
    """
    Build enhanced system prompt for selected thinking mode.
    
    Args:
        selected_mode: The selected thinking mode
        
    Returns:
        Enhanced system prompt
    """
    base_prompt = """You are an expert coastal hydrodynamics teaching assistant for a university course.
You have access to the full course textbooks and lecture slides via RAG retrieval.

Core Responsibilities:
1. Provide accurate, well-sourced answers
2. Show clear reasoning and mathematical derivations
3. Cite all sources and resources used
4. Adapt explanations to student's learning level"""
    
    mode_enhancement = get_thinking_mode_prompt(selected_mode)
    
    if mode_enhancement:
        return f"{base_prompt}\n\nReasoning Mode: {selected_mode.upper()}\n{mode_enhancement}"
    
    return base_prompt


def create_thinking_mode_tool():
    """Create tool for students to select thinking mode."""
    from langchain_core.tools import tool
    
    @tool
    def set_thinking_mode(mode: str) -> str:
        """
        Activate a specific thinking mode for the next question.
        
        Available modes:
        - standard: Normal reasoning
        - deep: Deep thinking with extended analysis
        - critical: Critical analysis with counterarguments
        - analytical: Step-by-step mathematical analysis
        - comprehensive: Multi-faceted comprehensive approach
        - mathematical: TOP-NOTCH mathematical rigor with complete derivations
        
        Args:
            mode: The thinking mode name
            
        Returns:
            Confirmation of activated mode
        """
        mode = mode.lower()
        valid_modes = [m.value for m in ThinkingMode]
        
        if mode not in valid_modes:
            return f"Invalid mode. Available: {', '.join(valid_modes)}"
        
        description = {
            "standard": "Normal reasoning - balanced and efficient",
            "deep": "Deep thinking - extended analysis and exploration",
            "critical": "Critical thinking - questioning and validation",
            "analytical": "Analytical - mathematical rigor and verification",
            "comprehensive": "Comprehensive - multi-disciplinary synthesis",
            "mathematical": "MATHEMATICAL EXCELLENCE - Complete derivations, verification, error analysis"
        }
        
        return f"✓ Activated {mode.upper()} thinking mode: {description[mode]}"
    
    return set_thinking_mode
