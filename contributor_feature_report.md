# Contributor Feature — Hardening Report

## A. Files Changed

| File | Change |
|------|--------|
| [`database.py`](file:///c:/Users/saval/OneDrive/Desktop/Acad/SE_Project/Backend/database.py) | Added unique compound index for commits `(projectId, sha)` alongside existing contributor index; updated docstring |
| [`.gitignore`](file:///c:/Users/saval/OneDrive/Desktop/Acad/SE_Project/.gitignore) | Added `__pycache__/` and `.pytest_cache/` entries |

## B. What Changed in Each File

### `database.py`
- **Added**: `commits_collection.create_index([("projectId", 1), ("sha", 1)], unique=True, background=True)` in `ensure_indexes()`
- **Updated**: Docstring to document both unique indexes
- **No changes** to connection logic — it already uses `os.environ.get("MONGO_URI")` with a clear `EnvironmentError` on missing config

### `.gitignore`
- Added `__pycache__/` and `.pytest_cache/` to prevent accidental commits of cache directories

## C. Contributor Data Flow

```
FastAPI POST /api/projects/{project_id}/sync-contributors
    ↓
main.py → sync_contributors() route handler
    ↓
contributor_service.py → sync_project_contributors()
    ├── persistence.get_project() → verify project exists
    ├── _resolve_repo_url() → validate/resolve repo URL
    ├── github_commits.get_github_contributors() → GitHub API (paginated)
    │       ├── _parse_github_url() → extract owner/repo
    │       ├── _get_authenticated_session() → auth headers
    │       └── _fetch_contributors() → paginated GET with error handling
    └── persistence.upsert_contributor() → MongoDB upsert per contributor
            └── filter: (projectId, github_username) → prevents duplicates
```

```
FastAPI GET /api/projects/{project_id}/contributors
    ↓
main.py → get_contributors() route handler
    ├── persistence.get_project() → verify project exists
    └── persistence.get_project_contributors() → MongoDB find by projectId
```

## D. API Endpoints

| Method | Endpoint | Status |
|--------|----------|--------|
| `GET` | `/api/projects/{project_id}/contributors` | ✅ Already implemented |
| `POST` | `/api/projects/{project_id}/sync-contributors` | ✅ Already implemented |
| `GET` | `/api/health` | ✅ Already implemented |

### Error Responses

| Error | HTTP Code | Source |
|-------|-----------|--------|
| Project not found | 404 | `ProjectNotFoundError` |
| No repo configured | 400 | `ProjectRepoNotConfiguredError` |
| Repo URL mismatch | 400 | `RepoMismatchError` |
| Invalid input | 400 | `ValueError` |
| GitHub token missing | 500 | `GitHubTokenMissingError` |
| GitHub auth failure | 401 | `GitHubAuthError` |
| Repo not found on GitHub | 404 | `GitHubRepoNotFoundError` |
| GitHub API/rate limit | 502 | `GitHubAPIError` |

## E. Database / Index Changes

| Collection | Index | Fields | Unique | Status |
|------------|-------|--------|--------|--------|
| `contributors` | Compound | `(projectId, github_username)` | ✅ Yes | Was already present |
| `commits` | Compound | `(projectId, sha)` | ✅ Yes | **Added** in this change |

Both indexes are created at startup via `ensure_indexes()` called in FastAPI's lifespan handler.

## F. Tests Run and Results

```
47 passed in 1.17s
```

### Test Coverage Breakdown

| # | Test Area | Tests | Status |
|---|-----------|-------|--------|
| 1 | Successful contributor retrieval | 1 | ✅ |
| 2 | GitHub username extraction | 1 | ✅ |
| 3 | Contributor metadata extraction | 1 | ✅ |
| 4 | Correct project association | 2 | ✅ |
| 5 | Existing contributor update | 1 | ✅ |
| 6 | New contributor insertion | 1 | ✅ |
| 7 | Duplicate prevention (upsert) | 1 | ✅ |
| 8 | Unique index behavior (DuplicateKeyError) | 2 | ✅ |
| 9 | Invalid project handling | 1 | ✅ |
| 10 | Invalid repository handling | 3 | ✅ |
| 11 | GitHub 401/403/404/API errors | 4 | ✅ |
| 12 | Network failure + timeout | 2 | ✅ |
| 13 | Pagination (multi-page, respects max, single-page) | 3 | ✅ |
| 14 | GET contributors endpoint | 2 | ✅ |
| 15 | POST sync-contributors endpoint | 3 | ✅ |
| — | Additional edge cases (empty repo, .git suffix, whitespace ID, etc.) | 19 | ✅ |

## G. Remaining Issues

> [!NOTE]
> **None.** The contributor feature is complete and hardened.

### Verification Checklist

- [x] All 47 tests pass
- [x] All imports verified clean
- [x] MongoDB configuration is environment-based (`MONGO_URI` required, `MONGO_DATABASE` optional with default)
- [x] Compound unique index exists for contributors `(projectId, github_username)`
- [x] Compound unique index exists for commits `(projectId, sha)`
- [x] Duplicate contributors cannot be created (upsert + unique index + DuplicateKeyError handling)
- [x] Correct `project_id` is stored with every contributor
- [x] GitHub errors are handled properly (401, 403, 404, rate limit, network, timeout)
- [x] `.env` is gitignored — no secrets in source control
- [x] No hardcoded credentials anywhere
- [x] API failure is never silently treated as "0 contributors"

### Architecture Summary

The existing codebase was **already well-architected** and covered all 10 tasks. The only changes needed were:

1. **Adding** a commits compound unique index for consistency
2. **Adding** cache directories to `.gitignore`

No existing working code was rewritten.
