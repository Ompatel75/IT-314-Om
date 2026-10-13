"""
FastAPI router for Contributor and Commit synchronization.

Endpoints:
    GET  /api/projects/{project_id}/contributors        – Retrieve stored contributors
    POST /api/projects/{project_id}/sync-contributors   – Sync contributors from GitHub
    GET  /api/projects/{project_id}/commits             – Retrieve stored commits
    POST /api/projects/{project_id}/sync-commits        – Sync commits from GitHub
"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from Backend.externalservies.commit_service import (
    get_commits_for_project,
    sync_project_commits,
)
from Backend.externalservies.contributor_service import (
    ProjectNotFoundError,
    ProjectRepoNotConfiguredError,
    RepoMismatchError,
    sync_project_contributors,
)
from Backend.externalservies.github_commits import (
    GitHubAPIError,
    GitHubAuthError,
    GitHubBranchNotFoundError,
    GitHubRepoNotFoundError,
    GitHubTokenMissingError,
)
from Backend.persistence import get_project, get_project_contributors

router = APIRouter(prefix="/api/projects", tags=["Data Sync"])


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
# Shared error mapper — avoids repeating the same except blocks everywhere
# ---------------------------------------------------------------------------

def _map_github_errors(exc: Exception) -> HTTPException:
    """Convert service-layer exceptions to appropriate HTTP responses."""
    if isinstance(exc, ProjectNotFoundError):
        return HTTPException(status_code=404, detail=str(exc))
    if isinstance(exc, (ProjectRepoNotConfiguredError, RepoMismatchError, ValueError)):
        return HTTPException(status_code=400, detail=str(exc))
    if isinstance(exc, GitHubTokenMissingError):
        return HTTPException(
            status_code=500,
            detail="GitHub token is not configured on the server.",
        )
    if isinstance(exc, GitHubAuthError):
        return HTTPException(
            status_code=401,
            detail="GitHub authentication failed. Check the configured token.",
        )
    if isinstance(exc, (GitHubRepoNotFoundError, GitHubBranchNotFoundError)):
        return HTTPException(status_code=404, detail=str(exc))
    if isinstance(exc, GitHubAPIError):
        return HTTPException(status_code=502, detail=str(exc))
    # Re-raise unknown exceptions — let FastAPI's default 500 handler take over
    raise exc


# ---------------------------------------------------------------------------
# Contributor endpoints
# ---------------------------------------------------------------------------

@router.get("/{project_id}/contributors", summary="List project contributors")
def get_contributors(project_id: str):
    """
    Retrieve the contributors stored for a project.

    Returns the list of GitHub contributors currently persisted in MongoDB
    for the given project. To refresh from GitHub, call sync-contributors first.
    """
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    return get_project_contributors(project_id)


@router.post("/{project_id}/sync-contributors", summary="Sync contributors from GitHub")
def sync_contributors(project_id: str, request: SyncContributorsRequest):
    """
    Sync contributors from GitHub for the given project.

    Uses the project's configured repository URL. If ``repo_url`` is
    provided in the request body it is validated against the project's
    stored configuration.
    """
    try:
        return sync_project_contributors(
            project_id=project_id,
            repo_url=request.repo_url,
        )
    except Exception as exc:
        raise _map_github_errors(exc)


# ---------------------------------------------------------------------------
# Commit endpoints
# ---------------------------------------------------------------------------

@router.get("/{project_id}/commits", summary="List project commits")
def get_commits(project_id: str):
    """
    Retrieve stored commits for a project.

    Returns all commits persisted in MongoDB for the given project.
    To ingest fresh commits from GitHub, call sync-commits first.
    """
    project = get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found.")
    try:
        return get_commits_for_project(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/{project_id}/sync-commits", summary="Sync commits from GitHub")
def sync_commits(project_id: str, request: SyncCommitsRequest):
    """
    Retrieve commits from GitHub and persist them for a project.

    The project's configured repository is used by default.
    If ``repo_url`` is supplied it must match the project's configured repository.
    If ``branch`` is omitted the repository's default branch is used.
    ``max_commits`` controls the maximum number of commits retrieved.
    GitHub pagination is handled transparently by the ingestion layer.
    """
    try:
        return sync_project_commits(
            project_id=project_id,
            repo_url=request.repo_url,
            branch=request.branch,
            max_commits=request.max_commits,
        )
    except Exception as exc:
        raise _map_github_errors(exc)
