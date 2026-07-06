import uuid

from langchain_core.tools import tool

from ..config import PLOTS_DIR
from .code_runner import run_code

PLOT_CODE_PROMPT = (
    "Generate only executable Python matplotlib code. "
    "You MUST save the final figure using: plt.savefig(_PLOT_PATH, dpi=150, bbox_inches='tight'). "
    "_PLOT_PATH is a pre-defined variable — do NOT redefine it. "
    "Do NOT call plt.show(). Do not wrap in if __name__ == '__main__'. "
    "Return ONLY the Python code, no markdown fences, no explanation."
)


def _get_plot_llm():
    """Lazy-load the plot LLM."""
    from ..retrieval import gcp_creds, _HAS_GCP
    if not _HAS_GCP or not gcp_creds:
        return None
    from langchain_google_vertexai import ChatVertexAI
    from ..config import GEMINI_MODEL, GCP_LOCATION, GCP_PROJECT
    return ChatVertexAI(
        model=GEMINI_MODEL,
        temperature=0.2,
        max_output_tokens=2048,
        credentials=gcp_creds,
        project=GCP_PROJECT,
        location=GCP_LOCATION,
    )


def _strip_fences(text: str) -> str:
    lines = text.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines)


@tool
def generate_plot(description: str, data_context: str = "") -> str:
    """Generate and return a matplotlib plot.
    Describe what to plot in plain English.
    Provide data_context with specific numerical values if needed.
    Returns PLOT_SAVED:<path> on success."""
    llm = _get_plot_llm()
    if llm is None:
        return "ERROR: Plot generation requires GCP credentials. Configure them in api/.env"

    from langchain_core.messages import HumanMessage

    plot_path = str(PLOTS_DIR / f"{uuid.uuid4().hex}.png")
    prompt = PLOT_CODE_PROMPT + "\n\nPlot request: " + description
    if data_context:
        prompt += "\n\nData:\n" + data_context

    code = _strip_fences(llm.invoke([HumanMessage(content=prompt)]).content)
    r = run_code(code, plot_path=plot_path)

    # Retry once on failure
    if not r["plot_path"] and r["stderr"]:
        retry_prompt = (
            prompt
            + "\n\nPrevious attempt failed:\n"
            + r["stderr"]
            + "\n\nFix the code and try again."
        )
        code2 = _strip_fences(
            llm.invoke([HumanMessage(content=retry_prompt)]).content
        )
        r = run_code(code2, plot_path=plot_path)

    if r["plot_path"]:
        return f"PLOT_SAVED:{r['plot_path']}\n{r['stdout']}"
    return r["stderr"] or "Plot generation failed with no error message."
