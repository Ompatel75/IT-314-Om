
"""
FastAPI router for Contributor and Commit synchronization.

Endpoints:
    GET  /api/projects/{project_id}/contributors
    POST /api/projects/{project_id}/sync-contributors
    GET  /api/projects/{project_id}/commits
    POST /api/projects/{project_id}/sync-commits
"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from Backend.auth.dependencies import get_current_user
from Backend.auth.roles import Role, require_role
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
from Backend.persistence import DatabaseError
from Backend.routers.project_router import (
    _get_user_id,
    _is_project_member,
)

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
# Shared authorization helper
# ---------------------------------------------------------------------------

def _require_project_member(
    project_id: str,
    current_user: dict,
) -> dict:
    """Require an authenticated project owner or member."""
    user_id = _get_user_id(current_user)

    project = get_project(project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    if not _is_project_member(project, user_id):
        raise HTTPException(
            status_code=403,
            detail="Access denied. You are not a member of this project.",
        )

    return project


# ---------------------------------------------------------------------------
# Shared error mapper
# ---------------------------------------------------------------------------

def _map_github_errors(exc: Exception) -> HTTPException:
    """Convert service-layer exceptions to appropriate HTTP responses."""
    if isinstance(exc, ProjectNotFoundError):
        return HTTPException(status_code=404, detail=str(exc))

    if isinstance(
        exc,
        (ProjectRepoNotConfiguredError, RepoMismatchError, ValueError),
    ):
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

    if isinstance(exc, DatabaseError):
        return HTTPException(
            status_code=503,
            detail=str(exc),
        )

    # For any other unexpected exception, return a generic 500 without
    # leaking internal implementation details to the client.
    return HTTPException(
        status_code=500,
        detail="An unexpected server error occurred. Please try again later.",
    )


# ---------------------------------------------------------------------------
# Contributor endpoints
# ---------------------------------------------------------------------------

@router.get("/{project_id}/contributors", summary="List project contributors")
def get_contributors(
    project_id: str,
    current_user: dict = Depends(get_current_user),
):
    """
    Retrieve stored contributors for a project.

    Requires authentication and verified project membership.
    """
    _require_project_member(project_id, current_user)
    return get_project_contributors(project_id)


@router.post(
    "/{project_id}/sync-contributors",
    summary="Sync contributors from GitHub",
)
def sync_contributors(
    project_id: str,
    request: SyncContributorsRequest,
    current_user: dict = Depends(
        require_role(Role.ADMIN, Role.PROJECT_MANAGER)
    ),
):
    """
    Sync contributors from GitHub.

    Requires authentication and verified project membership.
    """
    _require_project_member(project_id, current_user)

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
def get_commits(
    project_id: str,
    current_user: dict = Depends(get_current_user),
):
    """
    Retrieve stored commits for a project.

    Requires authentication and verified project membership.
    """
    _require_project_member(project_id, current_user)

    try:
        return get_commits_for_project(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/{project_id}/sync-commits", summary="Sync commits from GitHub")
def sync_commits(
    project_id: str,
    request: SyncCommitsRequest,
    current_user: dict = Depends(
        require_role(Role.ADMIN, Role.PROJECT_MANAGER)
    ),
):
    """
    Retrieve commits from GitHub and persist them.

    Requires authentication and verified project membership.
    """
    _require_project_member(project_id, current_user)

    try:
        return sync_project_commits(
            project_id=project_id,
            repo_url=request.repo_url,
            branch=request.branch,
            max_commits=request.max_commits,
        )
    except Exception as exc:
        raise _map_github_errors(exc)
