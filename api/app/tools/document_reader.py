import base64
from pathlib import Path

from langchain_core.tools import tool


def _get_vision_llm():
    """Lazy-load the vision LLM."""
    from ..retrieval import gcp_creds, _HAS_GCP
    if not _HAS_GCP or not gcp_creds:
        return None
    from langchain_google_vertexai import ChatVertexAI
    from ..config import GEMINI_MODEL, GCP_LOCATION, GCP_PROJECT
    return ChatVertexAI(
        model=GEMINI_MODEL,
        temperature=0.2,
        max_output_tokens=4096,
        credentials=gcp_creds,
        project=GCP_PROJECT,
        location=GCP_LOCATION,
    )


def _gemini_vision(image_bytes: bytes, mime: str, question: str) -> str:
    llm = _get_vision_llm()
    if llm is None:
        return "ERROR: Vision analysis requires GCP credentials. Configure them in api/.env"
    from langchain_core.messages import HumanMessage
    b64 = base64.b64encode(image_bytes).decode()
    msg = HumanMessage(content=[
        {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
        {"type": "text", "text": "You are a coastal hydrodynamics expert. " + question},
    ])
    return llm.invoke([msg]).content


@tool
def read_document(file_path: str, question: str, pages: str = "all") -> str:
    """Read and analyse a PDF or image file (jpg/png/jpeg).
    For PDFs: extracts text per page; uses Gemini vision for figure-heavy pages (<100 chars text).
    pages: 'all', a single page number '3', or a range '1-5'."""
    p = Path(file_path)
    if not p.exists():
        return f"ERROR: File not found: {file_path}"

    ext = p.suffix.lower()

    if ext in (".png", ".jpg", ".jpeg"):
        mime = "image/png" if ext == ".png" else "image/jpeg"
        return _gemini_vision(p.read_bytes(), mime, question)

    if ext == ".pdf":
        try:
            import fitz  # PyMuPDF
        except ImportError:
            return "ERROR: PyMuPDF (fitz) not installed. Run: pip install pymupdf"

        doc = fitz.open(str(p))
        total = len(doc)

        if pages == "all":
            page_indices = list(range(total))
        elif "-" in pages:
            s, e = pages.split("-")
            page_indices = list(range(int(s) - 1, min(int(e), total)))
        else:
            page_indices = [int(pages) - 1]

        parts = []
        for i in page_indices:
            page = doc[i]
            text = page.get_text()
            if len(text.strip()) >= 100:
                parts.append(f"[Page {i+1}]\n{text.strip()}")
            else:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                vision_ans = _gemini_vision(pix.tobytes("png"), "image/png", question)
                parts.append(f"[Page {i+1} – vision]\n{vision_ans}")
        doc.close()
        return "\n\n".join(parts)

    return f"ERROR: Unsupported file type: {ext}"
