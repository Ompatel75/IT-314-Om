"""
Implement:

    get_github_commit_history(
        repo_url: str,
        branch: str | None = None,
        max_commits: int = 30
    )

SETUP:
    - Create a .env file in the project root.
    - Add the GitHub Personal Access Token as:

        GITHUB_TOKEN=<your_github_token>

    - Load GITHUB_TOKEN from .env using python-dotenv.
    - Do NOT hardcode the token in Python code.
    - Add .env to .gitignore so the token is never committed.

INPUT:
    repo_url:
        Full GitHub repository URL.

    branch:
        Optional branch.
        If None, use the repository's default branch.

    max_commits:
        Maximum commits to retrieve. Default: 30.

REQUIREMENTS:
    - Use GITHUB_TOKEN for GitHub API authentication.
    - Retrieve repository information.
    - Detect default branch.
    - Use configured branch if provided.
    - Retrieve commit history.
    - Retrieve commit change statistics.

EACH COMMIT:
    - sha
    - short_sha
    - author
    - github_username
    - timestamp
    - message
    - additions
    - deletions
    - total_changes

OUTPUT:

{
    "success": True,
    "repository": {
        "owner": "...",
        "name": "...",
        "full_name": "...",
        "url": "..."
    },
    "branch": {
        "selected": "...",
        "default": "...",
        "was_configured": True/False
    },
    "commit_count": 0,
    "commits": [...]
}

ERROR HANDLING:
    - Missing GITHUB_TOKEN
    - Invalid/expired token
    - Repository not found/inaccessible
    - Branch not found
    - GitHub API/network failure

IMPORTANT:
    - Read-only operation.
    - Never expose, print, or hardcode the token.
    - Return normalized data, not raw GitHub API responses.
    - No AI/LLM, health, risk, database, or frontend logic.
    - Function must be importable by other modules.

FILES TO CREATE/MODIFY:
    - github_commit_service.py
    - .env
    - .gitignore

.env:
    GITHUB_TOKEN=<your_github_token>

.gitignore:
    .env

DEFINITION OF DONE:
    - .env authentication works.
    - Commit retrieval works.
    - Default/custom branch logic works.
    - Commit author, timestamp, and change statistics are returned.
    - Errors are handled.
    - Function is reusable/importable.
    - Basic unit tests are included.
"""