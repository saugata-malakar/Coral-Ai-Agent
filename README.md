# Coastal Hydrodynamics AI Teaching Assistant

Welcome to the **Coastal Hydrodynamics AI Teaching Assistant**, an advanced RAG-powered educational platform designed specifically for coastal engineering coursework.

## 🚀 Live Educational Platform

The application is successfully deployed and accessible via Google Cloud Run. Students and educators can access the live educational interface here:

**🌐 Website URL:** [https://coastal-agent-340217722521.us-central1.run.app](https://coastal-agent-340217722521.us-central1.run.app)

### 🔐 Demo Credentials

To access the platform, please use the following credentials:
- **Email:** `admin@test.com`
- **Password:** `admin123`

---

> **⚠️ Important Note Regarding Initial Load Time:**
> Upon your first visit (or after a period of inactivity), the application might take a little extra time to start up. This is normal behavior due to the system initializing and building up the cache. **Once the initial load is complete, the application will run smoothly and responsively.** Please be patient during this brief cold start!

---

## 🎓 About the Educational Platform

This website serves as an interactive teaching assistant for students learning coastal engineering and hydrodynamics. Built on top of robust AI models (Google Vertex AI / Gemini 2.5 Flash) and a LangGraph ReAct Agent architecture, it provides an immersive, data-driven educational experience. 

### Key Educational Features:

- **Intelligent Knowledge Retrieval:** Ask complex questions about wave mechanics, sediment transport, or coastal structures. The system uses a Hybrid Retrieval Architecture (Semantic + Keyword search) to instantly pull information from an extensive knowledge base of textbooks and lecture slides.
- **Multi-Modal Understanding:** The assistant can interpret diagrams, plots, and equations from textbooks using advanced vision-language models, making visual learning much more accessible.
- **On-Demand Computations:** Need to calculate wave celerity or solve numerical problems? The platform can execute Python code (NumPy/SciPy) in real-time to solve complex hydrodynamic equations and show the step-by-step logic.
- **Interactive Visualizations:** The assistant can generate custom visualizations to illustrate concepts like wave height transformation, tidal dynamics, or dispersion relations.
- **LaTeX Generation:** Easily generate professional LaTeX-formatted equations and documents for your assignments and research.
- **Document Analysis:** Upload your own PDFs or images for the AI assistant to read, analyze, and explain in simple terms.

## 🛠️ Technology Stack

- **Backend / Orchestration:** FastAPI, LangChain, LangGraph
- **AI Models:** Google Vertex AI (Gemini 2.5 Flash), InternVL2-2B (Vision Captioning)
- **Vector Database:** ChromaDB (Semantic Search), BM25 (Keyword Search)
- **Document Processing:** Marker-PDF (OCR-free parser)

## 📖 Additional Documentation

For comprehensive technical details, system architecture diagrams, data parsing pipelines, and further developer instructions, please refer to the `SYSTEM_DOCUMENTATION.md` included in the repository.
