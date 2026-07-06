"""
COASTAL AI AGENT — Main Entry Point
Serves both the FastAPI backend and the static HTML frontend.
"""
import os
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# LIFESPAN AND INITIALIZATION
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    logger.info("Starting Coastal AI Agent...")
    # Create demo user on startup
    _ensure_demo_user()
    yield
    logger.info("Shutting down Coastal AI Agent...")


def _ensure_demo_user():
    """Create the demo user (admin@test.com / admin123) if it doesn't exist."""
    try:
        from app.auth import UserDatabase
        from app.config import DATA_DIR
        db = UserDatabase(DATA_DIR)
        if not db.user_exists("admin@test.com"):
            user = db.create_user(
                email="admin@test.com",
                password="admin123",
                full_name="Demo Admin",
                roll_number="DEMO001"
            )
            logger.info(f"Demo user created: admin@test.com / admin123")
        else:
            logger.info("Demo user already exists")
    except Exception as e:
        logger.warning(f"Could not create demo user: {e}")

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
# STATIC FILES
# ============================================================================

static_path = Path(__file__).parent / "static"
logger.info(f"Serving static files from: {static_path}")

# ============================================================================
# API ROUTES — mounted WITHOUT /api prefix so frontend paths match
# ============================================================================

# Import routers
from app.routes import router as api_router
from app.auth_routes import router as auth_router

# The frontend calls /chat, /conversations, /plots, /compile-latex directly
# So we mount the API router WITHOUT a prefix
app.include_router(api_router, tags=["api"])

# Auth routes: /auth/login, /auth/signup, etc.
app.include_router(auth_router, tags=["auth"])


# ============================================================================
# HEALTH CHECK
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint for load balancer"""
    return {
        "status": "healthy",
        "service": "Coastal AI Agent",
        "version": "2.0"
    }


# ============================================================================
# FRONTEND ROUTES — SERVE STATIC HTML
# ============================================================================

@app.get("/")
async def read_root():
    """Serve main chat interface"""
    index_path = static_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")
    return JSONResponse({"message": "Coastal AI Agent API — frontend not found"})


@app.get("/login")
async def login_page():
    """Serve auth/login page"""
    auth_path = static_path / "auth.html"
    if auth_path.exists():
        return FileResponse(auth_path, media_type="text/html")
    return JSONResponse({"message": "Auth page not found"})


# ============================================================================
# CATCH-ALL FOR SPA ROUTING
# ============================================================================

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    """
    Catch all routes:
    - Serve static files if they exist
    - Otherwise serve index.html for client-side routing
    """
    # Don't catch API or auth routes
    if full_path.startswith("api/") or full_path.startswith("auth/"):
        raise HTTPException(status_code=404, detail="Not found")

    # Try to serve as a static file
    file_path = static_path / full_path
    if file_path.exists() and file_path.is_file():
        return FileResponse(file_path)

    # Fall back to index.html for SPA routing
    index_path = static_path / "index.html"
    if index_path.exists():
        return FileResponse(index_path, media_type="text/html")

    raise HTTPException(status_code=404, detail="Not found")


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Global HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))

    logger.info(f"Starting server on port {port}")
    logger.info(f"Open http://localhost:{port}/login to login")
    logger.info(f"Open http://localhost:{port}/ for the chat interface")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )
