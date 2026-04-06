"""
Entry point: uvicorn api.main:app --reload --port 8000
  or from inside api/: uvicorn main:app --reload --port 8000
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import PLOTS_DIR
from app.routes import cleanup_old_plots, router
from app.auth_routes import router as auth_router

STATIC_DIR = __file__[:__file__.rfind("/")] + "/static" if "/" in __file__ else "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: remove stale plots from previous sessions
    cleanup_old_plots()
    yield
    # Shutdown: nothing to do


app = FastAPI(title="Coastal Hydrodynamics Agent", version="1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes first (must be registered before the catch-all StaticFiles)
app.include_router(router)
app.include_router(auth_router)

# Serve generated plot images at /plots/<filename>
app.mount("/plots", StaticFiles(directory=str(PLOTS_DIR)), name="plots")

# Serve frontend (index.html + any assets) at /
# html=True means requests to "/" are served index.html automatically
from pathlib import Path as _Path
_static = _Path(__file__).parent / "static"
_static.mkdir(exist_ok=True)
app.mount("/", StaticFiles(directory=str(_static), html=True), name="static")
