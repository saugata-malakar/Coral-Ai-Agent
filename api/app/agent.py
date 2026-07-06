"""
LangGraph ReAct agent assembly and response runner.
Gracefully degrades if GCP credentials are not available.
"""
import logging
import re
import uuid
from pathlib import Path

from .config import GEMINI_MODEL, GCP_LOCATION, GCP_PROJECT, DATA_DIR
from .retrieval import gcp_creds, hybrid_search, _HAS_GCP
from .tools.thinking_modes import get_thinking_mode_system_prompt
from .tools.user_profile import UserProfileManager
from .tools.resource_tracker import ResourceTracker

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an EXPERT COASTAL HYDRODYNAMICS teaching assistant for university coursework.\n"
    "You deliver TOP-NOTCH answers with absolute mathematical rigor and accuracy.\n\n"
    
    "═══ MANDATORY CALCULATION PROTOCOL ═══\n"
    "1. ALWAYS CALL run_python for EVERY numerical computation.\n"
    "   - Never estimate or compute by hand\n"
    "   - ALWAYS verify results\n"
    "   - Report uncertainty and error bounds\n"
    "   - Show verification against known solutions\n\n"
    
    "2. ALWAYS USE symbolic and numerical tools:\n"
    "   - SymbolicCoastalMath.dispersion_relation() for wave equations\n"
    "   - SymbolicCoastalMath.wave_properties() for comprehensive wave analysis\n"
    "   - SymbolicCoastalMath.shoaling_refraction() for wave transformation\n"
    "   - SymbolicCoastalMath.radiation_stress() for momentum equations\n"
    "   - format_with_uncertainty() for proper uncertainty reporting\n\n"
    
    "3. DIMENSIONAL ANALYSIS:\n"
    "   - Check all equations dimensionally\n"
    "   - Verify consistent units throughout\n"
    "   - Report final answers in SI units with proper conversions\n"
    "   - Use COASTAL_CONSTANTS for standard values (g, rho_water, nu, etc.)\n\n"
    
    "4. VERIFICATION AND ERROR CHECKING:\n"
    "   - Always verify numerical solutions\n"
    "   - Report absolute and relative errors\n"
    "   - Check boundary conditions\n"
    "   - Validate physical reasonableness (e.g., kh thresholds for depth regimes)\n"
    "   - Use multiple methods when possible to cross-check\n\n"
    
    "5. STEP-BY-STEP MATHEMATICAL EXPOSITION (MANDATORY):\n"
    "   ### Step 1: Physical Context\n"
    "   Describe the phenomenon and relevant physics\n\n"
    "   ### Step 2: Given Parameters\n"
    "   List ALL given values with symbols and units in a table:\n"
    "   | Parameter | Symbol | Value | Unit |\n"
    "   |-----------|--------|-------|------|\n"
    "   | ... | ... | ... | ... |\n\n"
    "   ### Step 3: Governing Equations\n"
    "   Write ALL applicable equations in LaTeX:\n"
    "   $$\\text{Equation name and formula}$$\n"
    "   Explain each variable and its physical meaning.\n\n"
    "   ### Step 4: Detailed Solution Procedure\n"
    "   For EACH intermediate result:\n"
    "   **[Quantity Name] ($\\text{symbol}$):**\n"
    "   - Description: What this represents\n"
    "   - Formula: $$\\text{formula}$$\n"
    "   - Substitution: $$\\text{with values: } \\text{result}$$\n"
    "   - Verification: [Check if applicable]\n"
    "   - Units: [Confirm correct units]\n\n"
    "   ### Step 5: Verification Results\n"
    "   Report:\n"
    "   - Absolute error: [value]\n"
    "   - Relative error: [%]\n"
    "   - Solution valid: [Yes/No with justification]\n"
    "   - Physical reasonableness: [Checks passed]\n\n"
    "   ### Step 6: Final Answer Summary\n"
    "   Present all results in a comprehensive table with:\n"
    "   - Quantity name and symbol\n"
    "   - Computed value\n"
    "   - Units\n"
    "   - Uncertainty/error bounds\n"
    "   - Physical interpretation\n\n"
    
    "6. COASTAL-SPECIFIC RIGOR:\n"
    "   - Classify flow regime (deep/transitional/shallow) using kh criteria\n"
    "   - Account for frequency dispersion\n"
    "   - Include shoaling and refraction effects\n"
    "   - Report radiation stress components correctly\n"
    "   - Consider secondary effects (wave setup, streaming)\n\n"
    
    "═══ QUALITY STANDARDS ═══\n"
    "✓ Mathematical rigor: Every step justified and derived\n"
    "✓ Numerical accuracy: All calculations verified\n"
    "✓ Documentation: Every result with source and justification\n"
    "✓ Clarity: Complex concepts explained thoroughly\n"
    "✓ Completeness: Nothing omitted or assumed\n\n"
    
    "═══ SUPPORTING TOOLS ═══\n"
    "- rag_search: Find course materials and theory\n"
    "- run_python: Execute all calculations with SymbolicCoastalMath\n"
    "- generate_plot: Visualize results\n"
    "- latex_generator: Format equations\n"
    "- read_document: Process PDFs and images\n"
    "- generate_diagram: Create flowcharts and concept maps\n\n"
    
    "═══ FORMATTING ═══\n"
    "- Inline math: $E = \\frac{1}{8}\\rho g H^2$\n"
    "- Display math: $$\\omega^2 = gk\\tanh(kh)$$\n"
    "- Always include units: $H = 2.5 \\text{ m}$\n"
    "- Use tables for numerical results\n"
    "- Report final answer clearly highlighted\n\n"
    
    "CRITICAL: Every answer is COMPLETE, VERIFIED, and EXCELLENT in all directions."
)


def build_enhanced_system_prompt(
    thinking_mode: str = "standard",
    enable_web_search: bool = False,
    user_profile_info: str = ""
) -> str:
    """
    Build system prompt with thinking mode and feature enhancements.
    """
    prompt = SYSTEM_PROMPT
    
    # Add thinking mode enhancement
    mode_prompt = get_thinking_mode_system_prompt(thinking_mode)
    if thinking_mode != "standard":
        prompt = mode_prompt + "\n\n" + prompt
    
    # Add web search instructions if enabled
    if enable_web_search:
        prompt += (
            "\n\nWEB SEARCH CAPABILITY:\n"
            "10. You have access to web_search tool for real-time information.\n"
            "11. For current events, recent research, or real-world examples, consider using web_search.\n"
            "12. Always cite web sources with full URLs.\n"
            "13. For coastal engineering questions, prefer course materials but supplement with web search for recent developments.\n"
        )
    
    # Add user profile context if available
    if user_profile_info:
        prompt += f"\n\nUSER CONTEXT:\n{user_profile_info}\n"
    
    return prompt

# ── Sentinel used to replace empty Gemini responses ───────────────────────────
_SENTINEL = "(thinking)"

# ── LLM and Agent initialization ─────────────────────────────────────────────
_llm = None
_checkpointer = None
_agent = None
_enhanced_agent = None
_AGENT_AVAILABLE = False

# Initialize managers
_user_profile_manager = UserProfileManager(DATA_DIR)
_resource_tracker = ResourceTracker(DATA_DIR)

if _HAS_GCP and gcp_creds:
    try:
        from langchain_google_vertexai import ChatVertexAI
        from langgraph.checkpoint.memory import MemorySaver
        from langgraph.prebuilt import create_react_agent
        from .tools import ALL_TOOLS, get_enhanced_tools

        _llm = ChatVertexAI(
            model=GEMINI_MODEL,
            temperature=0.3,
            max_output_tokens=8192,
            credentials=gcp_creds,
            project=GCP_PROJECT,
            location=GCP_LOCATION,
        )
        _checkpointer = MemorySaver()
        _AGENT_AVAILABLE = True
        logger.info("LangGraph agent initialized with Vertex AI")
    except Exception as e:
        logger.warning(f"Failed to initialize LLM: {e}")
else:
    logger.info("GCP credentials not available — agent will use fallback mode")


def _guard_empty_response(response):
    """Intercept Gemini responses before they enter LangGraph state."""
    content = response.content
    is_empty = (
        not content
        or (isinstance(content, str) and not content.strip())
        or (
            isinstance(content, list)
            and not any(
                (
                    p.get("text", "").strip()
                    if isinstance(p, dict)
                    else (
                        p[1].strip()
                        if isinstance(p, tuple) and len(p) == 2 and p[0] == "text"
                        else str(p).strip()
                    )
                )
                for p in content
            )
        )
    )
    if is_empty:
        response.content = _SENTINEL
    return response


def _post_model_hook(state: dict) -> dict:
    """post_model_hook: runs after each LLM call inside the ReAct graph."""
    messages = state.get("messages", [])
    if not messages:
        return state
    last = messages[-1]
    last = _guard_empty_response(last)
    return {"messages": [*messages[:-1], last]}


def _get_agent(use_enhanced_tools: bool = False):
    """Get the agent, optionally with enhanced tools."""
    global _agent, _enhanced_agent

    if not _AGENT_AVAILABLE:
        return None

    from langgraph.prebuilt import create_react_agent
    from .tools import ALL_TOOLS, get_enhanced_tools as _get_enhanced

    if use_enhanced_tools:
        if _enhanced_agent is None:
            tools = _get_enhanced()
            _enhanced_agent = create_react_agent(
                _llm, tools, prompt=SYSTEM_PROMPT, checkpointer=_checkpointer,
                post_model_hook=_post_model_hook,
            )
        return _enhanced_agent
    else:
        if _agent is None:
            _agent = create_react_agent(
                _llm, ALL_TOOLS, prompt=SYSTEM_PROMPT, checkpointer=_checkpointer,
                post_model_hook=_post_model_hook,
            )
        return _agent


def _extract_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for p in content:
            if isinstance(p, dict):
                parts.append(p.get("text", ""))
            elif isinstance(p, tuple) and len(p) == 2:
                parts.append(p[1] if p[0] == "text" else "")
            else:
                parts.append(str(p))
        return "".join(parts)
    return str(content)


_PATH_RE = re.compile(
    r'FILE_\d+=\S+'
    r'|File\s+\d+\s+(path\s+\(use\s+EXACTLY\s+as-is\)|available\s+at):\s*\S+'
    r'|"?C:\\[^\s\n"<>]+'
    r'|/[\w/.-]+/uploads/[^\s\n]+',
    re.IGNORECASE,
)

_LATEX_RE = re.compile(r"(\\documentclass[\s\S]*?\\end\{document\})", re.DOTALL)


_SYNTH_RE = re.compile(
    r"Here are all the computed results from tools:.*?write the complete step-by-step solution with LaTeX math\.",
    re.DOTALL | re.IGNORECASE,
)


def _sanitize(text: str) -> str:
    """Strip file path references, sentinel placeholders, and synthesizer prompt leakage."""
    text = _PATH_RE.sub("", text)
    text = text.replace(_SENTINEL, "")
    text = _SYNTH_RE.sub("", text)
    return text.strip()



def _text_blocks_only(msg) -> str:
    """Extract text blocks from a message, skipping tool_use blocks."""
    content = msg.content
    if isinstance(content, list):
        parts = []
        for p in content:
            if isinstance(p, dict) and p.get("type") == "text":
                parts.append(p.get("text", ""))
            elif isinstance(p, tuple) and len(p) == 2 and p[0] == "text":
                parts.append(p[1])
        return "".join(parts).strip()
    return _extract_text(content).strip()


def _clear_session(session_id: str) -> None:
    """Wipe a corrupted MemorySaver thread so the next request starts clean."""
    if _checkpointer is None:
        return
    try:
        storage = _checkpointer.storage
        keys_to_delete = [k for k in storage if session_id in str(k)]
        for k in keys_to_delete:
            del storage[k]
    except Exception:
        pass


def _fallback_response(query: str) -> dict:
    """
    Provide a response when the LLM agent is not available.
    Uses RAG search to find relevant content and returns it directly.
    """
    # Try to find relevant content from the knowledge base
    results = hybrid_search(query, k=5)
    relevant_texts = [r["text"] for r in results if r.get("text", "").strip()]

    if relevant_texts:
        response = (
            "⚠️ **AI Agent Running in Offline Mode** (No GCP credentials configured)\n\n"
            "I found these relevant passages from the course materials:\n\n"
        )
        for i, text in enumerate(relevant_texts[:3], 1):
            # Truncate long texts
            excerpt = text[:500] + "..." if len(text) > 500 else text
            response += f"---\n\n**Source {i}:**\n{excerpt}\n\n"
        response += (
            "\n---\n\n"
            "💡 *To enable full AI-powered responses with step-by-step solutions, "
            "configure your GCP Vertex AI credentials in `api/.env`.*"
        )
    else:
        response = (
            "⚠️ **AI Agent Running in Offline Mode**\n\n"
            "The AI chat requires Google Cloud Vertex AI credentials to generate responses. "
            "To enable full functionality:\n\n"
            "1. Create a GCP service account with Vertex AI access\n"
            "2. Download the JSON key file\n"
            "3. Set `GCP_SA_KEY_PATH=path/to/key.json` in `api/.env`\n\n"
            "The rest of the application (auth, conversations, UI) works fully without credentials."
        )

    return {
        "text": response,
        "plots": [],
        "answer_id": None,
        "citations": None,
    }


def run_agent(
    query: str,
    session_id: str = "default",
    user_id: str = None,
    thinking_mode: str = "standard",
    enable_web_search: bool = False,
    enable_resource_citations: bool = True
) -> dict:
    """Run the agent on a query within a session."""

    # If agent is not available, use fallback
    if not _AGENT_AVAILABLE:
        return _fallback_response(query)

    # Build personalized system prompt
    user_profile_info = ""
    if user_id:
        profile = _user_profile_manager.get_profile(user_id)
        if profile.expertise_level != "beginner":
            user_profile_info = f"User expertise level: {profile.expertise_level}. Adjust technical depth accordingly."
    
    # Get system prompt with thinking mode and features
    system_prompt = build_enhanced_system_prompt(
        thinking_mode=thinking_mode,
        enable_web_search=enable_web_search,
        user_profile_info=user_profile_info
    )
    
    # Create the agent with appropriate tools
    use_enhanced = enable_web_search or thinking_mode != "standard"
    agent = _get_agent(use_enhanced_tools=use_enhanced)

    if agent is None:
        return _fallback_response(query)
    
    config = {"configurable": {"thread_id": session_id}}

    try:
        result = agent.invoke(
            {"messages": [("human", query)]},
            config=config,
        )
    except Exception as exc:
        err = str(exc)
        if "parts" in err.lower() or "400" in err:
            # Corrupted checkpoint — wipe session and retry once clean
            _clear_session(session_id)
            try:
                result = agent.invoke({"messages": [("human", query)]}, config=config)
            except Exception as e2:
                return _fallback_response(query)
        else:
            raise

    messages = result["messages"]

    # Find the last human message index to scope to this turn only
    last_human_idx = 0
    for i, msg in enumerate(messages):
        role = getattr(msg, "type", "") or getattr(msg, "role", "")
        if role in ("human", "user"):
            last_human_idx = i

    turn_msgs = messages[last_human_idx + 1:]

    # Pull clean LaTeX documents from tool messages
    latex_from_tools: list[str] = []
    for msg in turn_msgs:
        role = getattr(msg, "type", "") or getattr(msg, "role", "")
        if role == "tool":
            t = _extract_text(msg.content)
            for match in _LATEX_RE.finditer(t):
                latex_from_tools.append(match.group(1).strip())

    # ── Collect all AI text from this turn ───────────────────────────────────
    first_tool_idx = -1
    for i, msg in enumerate(turn_msgs):
        if (getattr(msg, "type", "") or getattr(msg, "role", "")) == "tool":
            first_tool_idx = i
            break

    response_parts = []
    for i, msg in enumerate(turn_msgs):
        role = getattr(msg, "type", "") or getattr(msg, "role", "")
        if role not in ("ai", "assistant"):
            continue
        if first_tool_idx >= 0 and i < first_tool_idx:
            continue  # skip pre-tool planning text
        t = _text_blocks_only(msg)
        if not t:
            t = _extract_text(msg.content).strip()
        t = _LATEX_RE.sub("", t).strip()
        t = _sanitize(t)
        if t:
            response_parts.append(t)
    response_text = "\n\n".join(response_parts)

    # ── Always synthesize final answer from tool outputs if agent was silent ──
    if not response_text and first_tool_idx >= 0:
        tool_texts = []
        for msg in turn_msgs:
            if (getattr(msg, "type", "") or getattr(msg, "role", "")) == "tool":
                t = _extract_text(msg.content).strip()
                if t and not t.startswith("ERROR"):
                    tool_texts.append(t)
        if tool_texts:
            from langchain_core.messages import HumanMessage, SystemMessage
            try:
                syn = _llm.invoke([
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=(
                        f"Original question: {query}\n\n"
                        "Here are all the computed results from tools:\n\n" +
                        "\n\n---\n\n".join(tool_texts) +
                        "\n\nWrite the complete step-by-step solution with LaTeX math. "
                        "Use ONLY the numerical values above — do not recompute. "
                        "Do NOT include Python code. Do NOT repeat these instructions. "
                        "Start directly with '### Step 1' and present only the mathematical solution."
                    )),
                ])
                t = _extract_text(syn.content).strip()
                # Strip any leaked synthesizer preamble
                for marker in [
                    "Here are all the computed results from tools:",
                    "Using ONLY these computed values",
                    "Original question:",
                    "Tool outputs:",
                ]:
                    idx = t.find(marker)
                    if idx != -1:
                        t = t[idx + len(marker):].strip()
                t = _LATEX_RE.sub("", t).strip()
                t = _sanitize(t)
                if t:
                    response_text = t
            except Exception as e:
                print(f"[agent] synthesizer failed: {e}")

    # Append clean LaTeX from tools
    if latex_from_tools:
        response_text = (response_text + "\n\n" if response_text else "") + "\n\n".join(latex_from_tools)

    # Collect plots
    plots = []
    for msg in result["messages"]:
        for match in re.finditer(r"PLOT_SAVED:([^\s\n]+)", _extract_text(msg.content)):
            path = match.group(1)
            if Path(path).exists():
                plots.append(path)

    # Store answer with citations if enabled
    answer_id = None
    citations = []
    if enable_resource_citations:
        answer_id = str(uuid.uuid4())
        # Save answer with citations
        _resource_tracker.save_answer_with_citations(
            question=query,
            answer_text=response_text,
            citations=citations,
            thinking_mode=thinking_mode,
            user_id=user_id,
            answer_id=answer_id
        )
    
    # Record user interaction if user_id provided
    if user_id:
        _user_profile_manager.record_interaction(
            user_id=user_id,
            question=query,
            thinking_mode=thinking_mode,
            topic_tags=[],
            answer_length=len(response_text)
        )

    return {
        "text": response_text,
        "plots": plots,
        "answer_id": answer_id,
        "citations": citations if enable_resource_citations else None
    }
