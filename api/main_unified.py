"""
UNIFIED COASTAL AI AGENT - Backend + Frontend Combined
Runs on Google Cloud Run
"""

import os
import logging
from pathlib import Path
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import app components
from app.agent import CoastalAgent
from app.config import Settings
from app.routes import router as api_router

# ============================================================================
# LIFESPAN AND INITIALIZATION
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("Starting Coastal AI Agent...")
    yield
    logger.info("Shutting down Coastal AI Agent...")

# ============================================================================
# CREATE FASTAPI APP
# ============================================================================

app = FastAPI(
    title="Coastal AI Agent API",
    description="AI-powered Coastal Engineering Assistant",
    version="2.0",
    lifespan=lifespan
)

# ============================================================================
# CORS CONFIGURATION
# ============================================================================

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://coastal-ai-agent.web.app",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# STATIC FILES - SERVE FRONTEND FROM BACKEND
# ============================================================================

static_path = Path(__file__).parent / "static"
if not static_path.exists():
    static_path = Path(__file__).parent.parent / "static"

logger.info(f"Serving static files from: {static_path}")

if static_path.exists():
    app.mount("/assets", StaticFiles(directory=str(static_path / "assets")), name="assets")

# ============================================================================
# API ROUTES
# ============================================================================

app.include_router(api_router, prefix="/api", tags=["api"])

@app.get("/health")
async def health_check():
    """Health check endpoint for load balancer"""
    return {
        "status": "healthy",
        "service": "Coastal AI Agent",
        "version": "2.0"
    }

# ============================================================================
# FRONTEND ROUTES - SERVE REACT APP
# ============================================================================

@app.get("/")
async def read_root():
    """Serve React index.html"""
    index_path = static_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")
    return {"message": "Coastal AI Agent API"}

@app.get("/auth/callback")
async def auth_callback():
    """OAuth callback endpoint"""
    index_path = static_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")
    return {"status": "callback received"}

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    """Catch all routes and serve index.html for React Router"""
    if full_path.startswith("api/") or full_path.startswith("assets/"):
        raise HTTPException(status_code=404, detail="Not found")
    
    index_path = static_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")
    
    raise HTTPException(status_code=404, detail="Not found")

# ============================================================================
# STARTUP EVENT
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    logger.info("Coastal AI Agent ready!")
    logger.info(f"Serving static files from: {static_path}")
    logger.info("API documentation: /docs")

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Global HTTP exception handler"""
    logger.error(f"HTTP Exception: {exc.detail}")
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    
    logger.info(f"Starting server on port {port}")
    logger.info("Unified Backend + Frontend Application")
    
    uvicorn.run(
        "main_unified:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        log_level="info"
    )
