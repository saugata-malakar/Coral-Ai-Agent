from typing import Optional

from langchain_core.tools import tool

TEXPERT_SYSTEM_PROMPT = (
    "You are an AI assistant designed to generate LaTeX code and respond to user requests "
    "across a wide range of document types, including letters, research papers, project proposals, "
    "stories, legal notices, and more. When users request modifications, provide the existing LaTeX "
    "code and make the specified changes clearly. If a user asks to include figures, provide the LaTeX "
    "code for graphics, ensuring to specify the filename, caption, and any relevant details. If a request "
    "is unclear or seems out of context, politely ask the user for clarification, and any such inquiries "
    "must be included as comments in the LaTeX code to avoid compilation errors. Maintain a professional "
    "and helpful tone, encouraging users to provide additional details if needed. Ensure all LaTeX responses "
    "are correctly formatted and ready for immediate use, without including example prompts or outputs "
    "directly, and ensure that any non-code text is commented appropriately to prevent errors during "
    "compilation. Absolutely do not include any text other than latex code or comments since whatever you "
    "respond with is directly put in the compiler and anything other than code will give a compilation error. "
    "Also dont put the ```latex markdown in your responses, since it is directly put in the "
    "compiler... in other words..just give the code... no need of markdown. "
    "CRITICAL: Generate only pdflatex-compatible LaTeX. Do NOT use fontspec, unicode-math, polyglossia, "
    "xltxtra, xunicode, or any other XeLaTeX/LuaLaTeX-specific packages. "
    "For encoding, use \\usepackage[utf8]{inputenc} and \\usepackage[T1]{fontenc}. "
    "Use only standard LaTeX2e packages compatible with pdflatex."
)

# Packages that only work with XeLaTeX/LuaLaTeX — trigger automatic compiler switch
XELATEX_PACKAGES = {"fontspec", "unicode-math", "polyglossia", "xltxtra", "xunicode"}


def _get_latex_llm():
    """Lazy-load the LaTeX LLM."""
    from ..retrieval import gcp_creds, _HAS_GCP
    if not _HAS_GCP or not gcp_creds:
        return None
    from langchain_google_vertexai import ChatVertexAI
    from ..config import GEMINI_MODEL, GCP_LOCATION, GCP_PROJECT
    return ChatVertexAI(
        model=GEMINI_MODEL,
        temperature=1.0,
        max_output_tokens=8192,
        credentials=gcp_creds,
        project=GCP_PROJECT,
        location=GCP_LOCATION,
    )


@tool
def latex_generator(description: str, existing_latex: str = "") -> str:
    """Generate LaTeX code for equations, full documents, or formatted content.
    Provide existing_latex when iteratively modifying a document.
    Returns raw LaTeX ready to compile."""
    llm = _get_latex_llm()
    if llm is None:
        return "ERROR: LaTeX generation requires GCP credentials. Configure them in api/.env"

    from langchain_core.messages import HumanMessage, SystemMessage

    user_msg = (existing_latex + "\n" + description) if existing_latex else description
    response = llm.invoke([
        SystemMessage(content=TEXPERT_SYSTEM_PROMPT),
        HumanMessage(content=user_msg),
    ])
    return response.content


def _try_compile(source: str, compiler: str) -> Optional[bytes]:
    """Attempt to compile LaTeX source using the given compiler via latex.ytotech.com."""
    import requests

    try:
        print(f"[LaTeX] Trying {compiler} via latex.ytotech.com...")
        response = requests.post(
            "https://latex.ytotech.com/builds/sync",
            json={
                "compiler": compiler,
                "resources": [{"main": True, "content": source}],
            },
            headers={"Content-Type": "application/json"},
            timeout=60,
        )
        print(f"[LaTeX] {compiler} status={response.status_code} first4={response.content[:4]}")
        if 200 <= response.status_code < 300 and response.content[:4] == b"%PDF":
            print(f"[LaTeX] {compiler} succeeded.")
            return response.content
        else:
            print(f"[LaTeX] {compiler} failed: {response.text[:300]}")
    except Exception as e:
        print(f"[LaTeX] {compiler} exception: {e}")
    return None


def compile_latex(source: str) -> tuple[Optional[bytes], Optional[str]]:
    """
    Compile LaTeX source to PDF.
    Auto-detects xelatex-specific packages and selects the right compiler first.
    Falls back to the alternative compiler on failure.
    Returns (pdf_bytes, error_message). pdf_bytes is None on failure.
    """
    needs_xelatex = any(
        f"\\usepackage{{{pkg}}}" in source or f"{{{pkg}}}" in source
        for pkg in XELATEX_PACKAGES
    )
    compilers = ["xelatex", "pdflatex"] if needs_xelatex else ["pdflatex", "xelatex"]

    for compiler in compilers:
        pdf = _try_compile(source, compiler)
        if pdf:
            return pdf, None

    return None, (
        "LaTeX compilation failed with both pdflatex and xelatex. "
        "Download the .tex file and compile locally, or check your LaTeX syntax."
    )
