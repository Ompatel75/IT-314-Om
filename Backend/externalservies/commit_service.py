"""
Commit Ingestion Service
------------------------

Orchestrates GitHub commit retrieval and persistence to MongoDB.

Flow:
    project_id
        -> Verify project exists
        -> Resolve and validate repository URL
        -> Retrieve commits from GitHub
        -> Add repository and branch context
        -> Upsert each commit into MongoDB
        -> Return ingestion summary

This service is used for Sprint 1 Issue #33:
Initial Commit Ingestion and Processing.
"""

from pymongo.errors import DuplicateKeyError

from Backend.externalservies.github_commits import (
    get_github_commit_history,
    GitHubTokenMissingError,
    GitHubAuthError,
    GitHubRepoNotFoundError,
    GitHubBranchNotFoundError,
    GitHubAPIError,
)

from Backend.persistence import (
    get_project,
    upsert_commit,
    get_project_commits,
)

from Backend.externalservies.contributor_service import (
    ProjectNotFoundError,
    ProjectRepoNotConfiguredError,
    RepoMismatchError,
    _resolve_repo_url,
)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def sync_project_commits(
    project_id: str,
    repo_url: str | None = None,
    branch: str | None = None,
    max_commits: int = 100,
) -> dict:
    """
    Retrieve commits from the project's GitHub repository and persist
    them to MongoDB.

    Existing commits are updated instead of inserted again because
    upsert_commit() uses (projectId, sha) as its unique identity.

    Args:
        project_id:
            MongoDB ObjectId string of the project.

        repo_url:
            Optional GitHub repository URL.

            If the project already has a configured repo_url, that URL
            is used and any provided repo_url must match it.

        branch:
            Optional branch to ingest.

            If None, get_github_commit_history() automatically uses the
            repository's default branch.

        max_commits:
            Maximum number of commits to retrieve from GitHub.

    Returns:
        Dictionary containing the ingestion result.

        Example:

        {
            "success": True,
            "project_id": "...",
            "repository": {...},
            "branch": {...},
            "synced_count": 10,
            "commits": [
                {
                    "commit_id": "...",
                    "sha": "...",
                    "short_sha": "...",
                    "author": "...",
                    "timestamp": "..."
                }
            ]
        }

    Raises:
        ValueError:
            If project_id is empty or max_commits is not positive.

        ProjectNotFoundError:
            If the project does not exist.

        ProjectRepoNotConfiguredError:
            If no repository URL is available.

        RepoMismatchError:
            If the provided repository does not match the project's
            configured repository.

        GitHubTokenMissingError:
            If GITHUB_TOKEN is missing.

        GitHubAuthError:
            If GitHub authentication fails.

        GitHubRepoNotFoundError:
            If the repository cannot be found.

        GitHubBranchNotFoundError:
            If the requested branch cannot be found.

        GitHubAPIError:
            For other GitHub API or network failures.
    """

    if not project_id or not project_id.strip():
        raise ValueError("project_id is required.")

    if max_commits <= 0:
        raise ValueError(
            "max_commits must be a positive integer."
        )

    # ---------------------------------------------------------------
    # 1. Verify that the project exists.
    # ---------------------------------------------------------------

    project = get_project(project_id)

    if not project:
        raise ProjectNotFoundError(
            f"Project '{project_id}' not found."
        )

    # ---------------------------------------------------------------
    # 2. Resolve the GitHub repository.
    #
    # Reuse the same repository validation logic as contributor sync
    # so both ingestion features behave consistently.
    # ---------------------------------------------------------------

    resolved_url = _resolve_repo_url(
        project,
        repo_url,
    )

    # ---------------------------------------------------------------
    # 3. Retrieve commits from GitHub.
    #
    # get_github_commit_history() handles:
    #   - repository validation
    #   - default branch detection
    #   - pagination
    #   - commit normalization
    #   - GitHub/network errors
    # ---------------------------------------------------------------

    result = get_github_commit_history(
        repo_url=resolved_url,
        branch=branch,
        max_commits=max_commits,
    )

    repository = result["repository"]
    branch_info = result["branch"]

    selected_branch = branch_info["selected"]
    default_branch = branch_info["default"]

    # ---------------------------------------------------------------
    # 4. Prepare and persist each commit.
    #
    # Repository and branch information are added to every commit
    # before it reaches the persistence layer.
    # ---------------------------------------------------------------

    synced = []

    for commit in result["commits"]:
        commit_record = {
            **commit,

            # Repository context
            "repository": repository["full_name"],
            "repository_url": repository["url"],

            # Branch context
            "branch": selected_branch,
            "default_branch": default_branch,
        }

        try:
            commit_id = upsert_commit(
                project_id,
                commit_record,
            )

        except DuplicateKeyError:
            # Normally upsert_commit() prevents duplicates because
            # (projectId, sha) is unique.
            #
            # This remains as a defensive safeguard against a race
            # condition where two ingestion operations attempt to
            # insert the same commit simultaneously.
            continue

        synced.append({
            "commit_id": commit_id,
            "sha": commit_record["sha"],
            "short_sha": commit_record["short_sha"],
            "author": commit_record["author"],
            "timestamp": commit_record["timestamp"],
        })

    # ---------------------------------------------------------------
    # 5. Return ingestion summary.
    # ---------------------------------------------------------------

    return {
        "success": True,
        "project_id": project_id,
        "repository": repository,
        "branch": branch_info,
        "synced_count": len(synced),
        "commits": synced,
    }


def get_commits_for_project(
    project_id: str,
) -> list[dict]:
    """
    Return commits currently stored for a project.

    Args:
        project_id:
            MongoDB ObjectId string of the project.

    Returns:
        List of serialized commit documents.

    Raises:
        ValueError:
            If project_id is empty.
    """

    if not project_id or not project_id.strip():
        raise ValueError("project_id is required.")

    return get_project_commits(project_id)