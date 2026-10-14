"""
FastAPI Application — AI Software Project Health & Risk Analyzer
-----------------------------------------------------------------
Entry point. Responsible for:
  - Application lifecycle (startup/shutdown)
  - Middleware configuration
  - Router registration

All business logic lives in the router modules:
  Backend/auth/router.py            – /auth/*
  Backend/routers/project_router.py – /api/projects  (CRUD)
  Backend/routers/data_sync_router.py – /api/projects/{id}/contributors | commits

Start with:
    uvicorn Backend.main:app --reload
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.auth.router import router as auth_router
from Backend.database import ensure_indexes
from Backend.routers.data_sync_router import router as data_sync_router
from Backend.routers.project_router import router as project_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup / shutdown lifecycle."""
    ensure_indexes()
    yield


app = FastAPI(
    title="AI Software Project Health & Risk Analyzer",
    version="0.1.0",
    description="Backend API for analysing software project health and risk.",
    lifespan=lifespan,
)

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(data_sync_router)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

@app.get("/api/health", tags=["Health"])
@app.get("/health", tags=["Health"])
def health_check():
    """Basic liveness probe endpoint."""
    return {"status": "healthy"}
