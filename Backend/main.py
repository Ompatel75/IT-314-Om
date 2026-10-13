"""
FastAPI Application — AI Software Project Health & Risk Analyzer
-----------------------------------------------------------------
Main API entry point combining Authentication, Contributor,
and GitHub Commit Ingestion features.

Contributor endpoints:
    GET  /api/projects/{project_id}/contributors
    POST /api/projects/{project_id}/sync-contributors

Commit endpoints:
    GET  /api/projects/{project_id}/commits
    POST /api/projects/{project_id}/sync-commits

Start with:
    uvicorn Backend.main:app
"""

from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Backend.auth.router import router as auth_router
from Backend.database import ensure_indexes
from Backend.persistence import get_project, get_project_contributors

from Backend.externalservies.contributor_service import (
    ProjectNotFoundError,
    ProjectRepoNotConfiguredError,
    RepoMismatchError,
    sync_project_contributors,
)

from Backend.externalservies.commit_service import (
    sync_project_commits,
    get_commits_for_project,
)

from Backend.externalservies.github_commits import (
    GitHubAPIError,
    GitHubAuthError,
    GitHubRepoNotFoundError,
    GitHubTokenMissingError,
    GitHubBranchNotFoundError,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup/shutdown lifecycle."""
    ensure_indexes()
    yield


app = FastAPI(
    title="AI Software Project Health & Risk Analyzer",
    version="0.1.0",
    description="Backend API for analysing software project health and risk.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------

from Backend.routers.project_router import router as project_router

app.include_router(auth_router)
app.include_router(project_router)


# ---------------------------------------------------------------------------
# Request models
# ---------------------------------------------------------------------------

class SyncContributorsRequest(BaseModel):
    repo_url: Optional[str] = None


class SyncCommitsRequest(BaseModel):
    repo_url: Optional[str] = None
    branch: Optional[str] = None
    max_commits: int = 100


# ---------------------------------------------------------------------------
# Health check endpoints
# ---------------------------------------------------------------------------

@app.get("/api/health")
@app.get("/health", tags=["Health"])
def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy"}


# ---------------------------------------------------------------------------
# Contributor endpoints
# ---------------------------------------------------------------------------

@app.get("/api/projects/{project_id}/contributors", tags=["Contributors"])
def get_contributors(project_id: str):
    """
    Retrieve stored contributors for a project.
    """
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return get_project_contributors(project_id)


@app.post("/api/projects/{project_id}/sync-contributors", tags=["Contributors"])
def sync_contributors(project_id: str, request: SyncContributorsRequest):
    """
    Sync contributors from GitHub for the given project.

    Uses the project's configured repository URL. If ``repo_url`` is
    provided in the request body it is validated against the project's
    stored configuration.
    """
    try:
        result = sync_project_contributors(
            project_id=project_id,
            repo_url=request.repo_url,
        )
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ProjectNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ProjectRepoNotConfiguredError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RepoMismatchError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except GitHubTokenMissingError:
        raise HTTPException(
            status_code=500,
            detail="GitHub token is not configured on the server.",
        )
    except GitHubAuthError:
        raise HTTPException(
            status_code=401,
            detail="GitHub authentication failed. Check the configured token.",
        )
    except GitHubRepoNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except GitHubAPIError as e:
        raise HTTPException(status_code=502, detail=str(e))


# ---------------------------------------------------------------------------
# Commit endpoints
# ---------------------------------------------------------------------------

@app.get("/api/projects/{project_id}/commits")
def get_commits(project_id: str):
    """
    Retrieve stored commits for a project.
    """
    project = get_project(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    try:
        return get_commits_for_project(project_id)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@app.post("/api/projects/{project_id}/sync-commits")
def sync_commits(
    project_id: str,
    request: SyncCommitsRequest,
):
    """
    Retrieve commits from GitHub and persist them for a project.

    The project's configured repository is used by default.

    If ``repo_url`` is supplied, it must match the repository
    configured for the project.

    If ``branch`` is omitted, the repository's default branch is used.

    ``max_commits`` controls the maximum number of commits retrieved.
    GitHub pagination is handled by the ingestion layer.
    """
    try:
        return sync_project_commits(
            project_id=project_id,
            repo_url=request.repo_url,
            branch=request.branch,
            max_commits=request.max_commits,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    except ProjectNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    except ProjectRepoNotConfiguredError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    except RepoMismatchError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    except GitHubTokenMissingError:
        raise HTTPException(
            status_code=500,
            detail="GitHub token is not configured on the server.",
        )
    except GitHubAuthError:
        raise HTTPException(
            status_code=401,
            detail="GitHub authentication failed. Check the configured token.",
        )
    except GitHubRepoNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    except GitHubBranchNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    except GitHubAPIError as e:
        raise HTTPException(
            status_code=502,
            detail=str(e),
        )
    except GitHubAPIError as e:
        raise HTTPException(
            status_code=502,
            detail=str(e),
        )
