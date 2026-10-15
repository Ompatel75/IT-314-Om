# AI Software Project Health & Risk Analyzer

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB_Atlas-Cloud_DB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![Tests Passing](https://img.shields.io/badge/Tests-183%20Passed%20(100%25)-brightgreen?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Agile Scrum](https://img.shields.io/badge/Agile-SCRUM%20Process-orange?style=for-the-badge)](./documents/9_Sprint_Plan.md)
[![Evaluation](https://img.shields.io/badge/Milestone-Mid--Evaluation%20Ready-blueviolet?style=for-the-badge)](#mid-evaluation-milestone-status)

> **An intelligent, data-driven platform that connects with software development workflows (GitHub repositories, commits, pull requests, issues, and sprint artifacts) to evaluate project health, detect delivery bottlenecks and workload imbalances, and generate grounded GenAI risk intelligence and actionable executive recommendations.**

---

## 📌 Mid-Evaluation Milestone Status

> **Evaluation Phase:** Mid-Term Evaluation  
> **Backend Architecture:** Production-Ready FastAPI with Microservice Separation  
> **Test Status:** ✅ **183 / 183 Tests Passing (100% Pass Rate)**  
> **Containerization:** ✅ **Fully Dockerized & Validated with Compose**  
> **Database:** ✅ **MongoDB Atlas with Compound Unique Indexing**  
> **Live API Documentation:** Interactive Swagger UI at `http://localhost:8000/docs`

### Deliverable Summary (Sprint 1 & Sprint 2 Ingestion Complete)

| Milestone Area | Status | Verification & Evidence |
| :--- | :---: | :--- |
| **Requirements & Elicitation** | ✅ **Done** | [10 Elicitation & Planning Specs](./documents/) across 6 Stakeholder groups |
| **Authentication & Security** | ✅ **Done** | JWT authentication, bcrypt hashing, stateless token management (`/auth/*`) |
| **Role-Based Access Control (RBAC)**| ✅ **Done** | 5 granular roles (`admin`, `owner`, `lead`, `member`, `viewer`) with route guards |
| **Project Management Service** | ✅ **Done** | Full CRUD for project lifecycle & repository association (`/api/projects`) |
| **GitHub Data Synchronization** | ✅ **Done** | Live commit & contributor ingestion, pagination, rate-limit handling |
| **Cloud Persistence & Indexing** | ✅ **Done** | MongoDB Atlas with compound unique keys: `(projectId, sha)`, `(projectId, github_username)` |
| **Data Redaction & Sanitization**| ✅ **Done** | Production logging filter masking tokens, passwords, secrets, and Mongo URIs |
| **Containerization & CI/CD** | ✅ **Done** | Multi-stage `Dockerfile`, `docker-compose.yml`, non-root execution |
| **Automated Testing Suite** | ✅ **Done** | **183 automated tests** covering unit, integration, and security layers |

---

## 📖 Table of Contents

- [Problem Statement & Vision](#-problem-statement--vision)
- [System Architecture](#-system-architecture)
- [Demonstrable Features (Mid-Evaluation)](#-demonstrable-features-mid-evaluation)
- [API Endpoints Directory](#-api-endpoints-directory)
- [Software Engineering & Agile Process](#-software-engineering--agile-process)
- [Quick Start & Setup Guide](#-quick-start--setup-guide)
- [Test Suite & Quality Verification](#-test-suite--quality-verification)
- [Database Schema & Design](#-database-schema--design)
- [Mid-Evaluation vs Final Roadmap](#-mid-evaluation-vs-final-roadmap)
- [Project Directory Structure](#-project-directory-structure)
- [Team Members & Contributions](#-team-members--contributions)

---

## 🎯 Problem Statement & Vision

### The Problem
Modern software development generates immense operational telemetry scattered across disparate platforms—commits, branch activities, code reviews, issue discussions, and sprint boards. Engineering leads and project managers struggle to synthesize this raw data:
- **Invisible Delivery Bottlenecks:** Pull requests languish in review queues undetected.
- **Workload Imbalances & Burnout:** Commit velocity and issue volume disproportionately fall on a few core contributors without management awareness.
- **Schedule Slippage:** Stale milestones and drift between sprint commitments and repository activity trigger unexpected release delays.
- **Superficial Metrics:** Existing dashboards calculate vanity metrics (lines of code, commit counts) without providing explainable reasons or remediation paths.

### Our Solution
The **AI Software Project Health & Risk Analyzer** combines deterministic metric computation with grounded GenAI reasoning:
1. **Connect & Synchronize:** Ingests live telemetry from GitHub repositories without cloning entire codebases.
2. **Deterministic Metric Engine:** Computes transparent, explainable health scores (bus factor risk, review latency, commit volatility).
3. **GenAI Advisory Layer:** Uses bounded LLM workflows to translate quantitative thresholds into human-understandable risk narratives and prescriptive actions.
4. **Role-Tailored Dashboards:** Provides appropriate views for individual developers, team leads, scrum masters, and executive stakeholders.

---

## 🏗 System Architecture

```text
                                 ┌─────────────────────────┐
                                 │   Frontend Application   │
                                 │   (React.js / Swagger)  │
                                 └────────────┬────────────┘
                                              │ HTTP / JSON
                                              ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                FastAPI Backend Service                                 │
│                                                                                        │
│  ┌────────────────────────────┐  ┌────────────────────────────┐  ┌──────────────────┐  │
│  │   Authentication & RBAC    │  │ Project Lifecycle Service  │  │  Secret Masking  │  │
│  │  (JWT / Bcrypt / 5 Roles)  │  │   (CRUD / Ownership Valid) │  │  Logging Filter  │  │
│  └─────────────┬──────────────┘  └─────────────┬──────────────┘  └─────────┬────────┘  │
│                │                               │                           │           │
│                └───────────────────────┬───────┴───────────────────────────┘           │
│                                        ▼                                               │
│                         ┌─────────────────────────────┐                                │
│                         │  GitHub Data Ingestion Bus  │                                │
│                         │ (Commits, Contribs, Issues) │                                │
│                         └──────────────┬──────────────┘                                │
└────────────────────────────────────────┼───────────────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
     ┌─────────────────────────────┐           ┌─────────────────────────────┐
     │      GitHub REST API        │           │    MongoDB Atlas Cluster    │
     │  - Rate-limiting handler    │           │  - Users & Projects         │
     │  - Token authentication     │           │  - Deduplicated Commits     │
     │  - Pagination traversal     │           │  - Contributors Directory   │
     └─────────────────────────────┘           └─────────────────────────────┘
                    │                                         │
                    └────────────────────┬────────────────────┘
                                         │ (Sprint 3 Pipeline)
                                         ▼
                         ┌───────────────────────────────┐
                         │   Deterministic Risk Engine   │
                         │   + GenAI LangGraph Workflow  │
                         └───────────────────────────────┘
```

---

## ⚡ Demonstrable Features (Mid-Evaluation)

### 1. Robust Authentication & User Management (`/auth`)
- **Self-Service Registration:** `/auth/signup` with validation, bcrypt password hashing, and duplicate email prevention.
- **Secure Token Generation:** `/auth/login` issuing HMAC-SHA256 JWT bearer tokens.
- **Identity Introspection:** `/auth/me` providing authenticated user session data and system role assignments.

### 2. Role-Based Access Control (RBAC)
- Five distinct system roles: `admin`, `owner`, `lead`, `member`, and `viewer`.
- Declarative route-level authorization dependencies (`require_role(...)`).
- Comprehensive permission boundary enforcement preventing unauthorized data modifications.

### 3. Project Lifecycle Management (`/api/projects`)
- Multi-project creation and tracking linked to authenticated creator accounts.
- Configuration of target GitHub repositories (`githubRepoUrl`, default branches, sprint settings).
- Access control validation: Projects can only be accessed by owners or assigned team members.
- Configurable update endpoints allowing owners to modify tracking settings.

### 4. GitHub Telemetry & Data Ingestion Engine
- **Live Commit Synchronization (`/api/projects/{id}/sync-commits`):**
  - Connects to GitHub API using personal access tokens.
  - Ingests commit SHA, author name, timestamp, message, and branch pointers.
  - Automatically deduplicates commits using MongoDB Atlas compound unique indexing `(projectId, sha)`.
- **Live Contributor Synchronization (`/api/projects/{id}/sync-contributors`):**
  - Fetches repository contributors with pagination.
  - Extracts contributor login, avatar URL, profile link, and contribution counts.
  - Deduplicates records using unique composite keys `(projectId, github_username)`.

### 5. Enterprise Security & Hardening
- **Automated Secret Redaction:** Custom logging filter intercepts and masks tokens, passwords, API keys, and connection strings from console output.
- **Centralized Exception Handling:** Standardized RFC-compliant JSON error responses across database failures, validation errors, and upstream GitHub outages.
- **CORS Configuration:** Safe cross-origin resource sharing configured for development and production origins.

---

## 🔌 API Endpoints Directory

All endpoints are demonstrable in real-time via the interactive Swagger interface at `http://localhost:8000/docs`:

| Tag | Method | Endpoint | Auth | Description |
| :--- | :---: | :--- | :---: | :--- |
| **System** | `GET` | `/api/health` | Public | System status, version info, and environment sanity check |
| **Auth** | `POST` | `/auth/signup` | Public | Register new user account with hashed credentials |
| **Auth** | `POST` | `/auth/login` | Public | Authenticate user and receive JWT access token |
| **Auth** | `POST` | `/auth/logout` | Public | Stateless session logout |
| **Auth** | `GET` | `/auth/me` | Bearer | Retrieve profile information and role of authenticated user |
| **Projects** | `POST` | `/api/projects` | Bearer | Create a new project and assign caller as owner |
| **Projects** | `GET` | `/api/projects` | Bearer | List all projects belonging to or shared with current user |
| **Projects** | `GET` | `/api/projects/{id}` | Bearer | Retrieve project metadata and GitHub integration settings |
| **Projects** | `PATCH` | `/api/projects/{id}` | Bearer (Owner) | Update project name, description, or repository target |
| **Data Sync**| `GET` | `/api/projects/{id}/contributors` | Bearer | Retrieve ingested contributors for a project |
| **Data Sync**| `POST` | `/api/projects/{id}/sync-contributors` | Bearer | Trigger live GitHub API sync for repository contributors |
| **Data Sync**| `GET` | `/api/projects/{id}/commits` | Bearer | Retrieve paginated list of ingested repository commits |
| **Data Sync**| `POST` | `/api/projects/{id}/sync-commits` | Bearer | Trigger live GitHub API ingestion for repository commits |

---

## 📋 Software Engineering & Agile Process

This project is developed strictly adhering to **Agile (SCRUM)** methodology and Software Engineering best practices. Complete documentation is maintained in the [`documents/`](./documents/) directory:

```
documents/
├── 1_Stakeholders.md                         # 6 Key Stakeholder Groups & Personas
├── 2_Elicitation_Tech.md                     # Elicitation Techniques (Interviews, Prototyping)
├── 3_Functional_Requirements.md              # FR Specifications (FR-01 through FR-18)
├── 4_NFR_Requirements.md                     # Non-Functional Requirements (Security, Performance)
├── 5_Domain_Requirements.md                  # Software Engineering & Git Domain Rules
├── 6_User_Stories_and_Acceptance_Criteria.md # Complete Backlog with INVEST Criteria
├── 7_Product_Backlog_Story_Points_Priority.md# Sizing & Story Point Estimations (110 pts total)
├── 8_Product_Epics.md                        # Epic Breakdown (E1 through E5)
├── 9_Sprint_Plan.md                          # 4-Sprint Cadence & Milestone Schedule
├── Final_Elicitation.md                      # Consolidated Requirement Elicitation Record
└── contributor_feature_report.md             # Contributor Feature Implementation & Testing
```

### Stakeholder Groups Addressed
1. **Individual Developers:** Transparent, activity-based signals without subjective judgment; feedback and appeal workflow.
2. **Code Reviewers / Senior Engineers:** Visibility into PR review queues and review latency bottlenecks.
3. **Engineering / Team Leads:** Bird's-eye project health, workload distribution metrics, and actionable recommendations.
4. **Scrum Masters / Agile Coaches:** Sprint burndown velocity, blocker alerts, and schedule slippage indicators.
5. **Project Managers:** Executive status summaries, milestone risks, and PDF report exports.
6. **System Administrators / DevOps Engineers:** RBAC controls, token rotation, audit logging, and Dockerized lifecycle.

---

## 🚀 Quick Start & Setup Guide

### Option 1: Running with Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OpenTirZ/Ai-Software-Project-Health-and-Risk-Analyzer.git
   cd Ai-Software-Project-Health-and-Risk-Analyzer
   ```

2. **Configure environment variables:**
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Ensure your `.env` contains:
   ```env
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
   MONGO_DATABASE=project_health
   JWT_SECRET_KEY=your-secure-random-secret-key-at-least-32-chars
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=1440
   GITHUB_TOKEN=your_github_personal_access_token
   ```

3. **Start the application container:**
   ```bash
   docker compose up --build
   ```

4. **Access the application:**
   - Interactive Swagger API: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Alternative ReDoc API: [http://localhost:8000/redoc](http://localhost:8000/redoc)
   - Healthcheck: [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

### Option 2: Running Locally with Python 3.12+

1. **Set up virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux / macOS:
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**
   ```bash
   uvicorn Backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## 🧪 Test Suite & Quality Verification

Quality is enforced via an extensive **pytest** test suite with **100% mocked external dependencies** (no accidental cloud writes or live GitHub API quota consumption during testing).

### Running Tests in Docker
```bash
docker compose run --rm backend pytest -v
```

### Test Results Breakdown (183 Passing Tests)

```text
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /app
plugins: mock-3.16.0, anyio-4.12.1
collected 183 items

Backend/auth/test_auth.py .................................... [ 32%]
Backend/auth/test_roles.py .....                               [ 35%]
Backend/test_contributor_service.py .......................... [ 61%]
Backend/test_github_commits.py ............................... [ 82%]
Backend/tests/test_project_management.py ..................... [100%]

============================= 183 passed in 23.30s =============================
```

- `test_auth.py` (60 tests): Signup, login, password hashing, token expiration, authorization header verification.
- `test_roles.py` (5 tests): Role hierarchy, permission matrix, forbidden role restrictions.
- `test_contributor_service.py` (47 tests): Contributor synchronization, duplicate prevention, GitHub error translations.
- `test_github_commits.py` (39 tests): Commit parsing, author resolution, pagination handling, network timeout resilience.
- `test_project_management.py` (32 tests): Project CRUD, ownership validation, tenant isolation, invalid ID protection.

---

## 🗄 Database Schema & Design

The system utilizes **MongoDB Atlas** with pre-configured compound unique indexing to guarantee data integrity across asynchronous ingestions:

```text
Database: project_health
├── users
│   ├── _id (ObjectId)
│   ├── name, email (unique), password_hash, role
│   └── createdAt, updatedAt
├── projects
│   ├── _id (ObjectId)
│   ├── name, description, githubRepoUrl
│   ├── ownerId, members (array of user IDs)
│   └── syncStatus, lastSyncedAt, createdAt
├── commits
│   ├── _id (ObjectId)
│   ├── projectId (Ref -> projects._id)
│   ├── sha (Git Commit Hash)
│   ├── author (name, email, date)
│   ├── message, branch
│   └── ⚠️ Compound Index: (projectId: 1, sha: 1) [UNIQUE]
└── contributors
    ├── _id (ObjectId)
    ├── projectId (Ref -> projects._id)
    ├── github_username, avatar_url, html_url, contributions
    └── ⚠️ Compound Index: (projectId: 1, github_username: 1) [UNIQUE]
```

---

## 🗺 Mid-Evaluation vs Final Roadmap

```
Sprint 1: System Foundation & Security      [████████████████████] 100% (Completed)
Sprint 2: Activity Telemetry & Ingestion    [████████████████░░░░]  80% (In Progress)
  ├── Live Commit Ingestion                 ✅ Done
  ├── Live Contributor Ingestion            ✅ Done
  ├── Pull Request & Review Ingestion       🔄 Scheduled
  └── Issue & Sprint Task Tracking          🔄 Scheduled
Sprint 3: Health Metric Engine & GenAI      [░░░░░░░░░░░░░░░░░░░░]   0% (Upcoming)
  ├── Bus Factor & Workload Balance Engine  🔄 Next Sprint
  ├── Bottleneck & Stale PR Detection       🔄 Next Sprint
  ├── LangGraph GenAI Analysis Pipeline     🔄 Next Sprint
  └── PDF Status Report Generation          🔄 Next Sprint
Sprint 4: UI Dashboard & Final Deployment   [░░░░░░░░░░░░░░░░░░░░]   0% (Upcoming)
  ├── React.js Interactive Dashboard        🔄 Planned
  ├── Real-time Alerts & Slack Delivery     🔄 Planned
  └── Production Cloud Deployment           🔄 Planned
```

---

## 📁 Project Directory Structure

```text
Ai-Software-Project-Health-and-Risk-Analyzer/
├── Backend/
│   ├── auth/                        # JWT & RBAC Authentication Module
│   │   ├── dependencies.py          # FastApi get_current_user injection
│   │   ├── roles.py                 # RBAC definitions & permission checkers
│   │   ├── router.py                # /auth/* endpoint definitions
│   │   ├── schemas.py               # Pydantic auth validation models
│   │   ├── security.py              # Bcrypt hashing & JWT encoding/decoding
│   │   ├── test_auth.py             # Auth test suite
│   │   └── test_roles.py            # RBAC test suite
│   ├── externalservies/             # Third-Party Integrations
│   │   ├── commit_service.py        # Commit business logic & sync
│   │   ├── contributor_service.py   # Contributor aggregation & sync
│   │   └── github_commits.py        # GitHub REST client with pagination
│   ├── routers/                     # Core Business API Routers
│   │   ├── data_sync_router.py      # /api/projects/{id}/sync-commits | contributors
│   │   └── project_router.py        # /api/projects CRUD endpoints
│   ├── schemas/                     # Shared Pydantic Models
│   │   └── project_schemas.py       # Project payload schemas
│   ├── tests/                       # Integration & End-to-End Tests
│   │   └── test_project_management.py
│   ├── database.py                  # PyMongo connection & index management
│   ├── persistence.py               # Repository data access layer (DAO)
│   ├── test_contributor_service.py  # Contributor service unit tests
│   ├── test_github_commits.py       # GitHub ingestion unit tests
│   └── main.py                      # FastAPI App initialization & middleware
├── documents/                       # Software Engineering & Agile Documentation
│   ├── 1_Stakeholders.md
│   ├── 2_Elicitation_Tech.md
│   ├── 3_Functional_Requirements.md
│   ├── 4_NFR_Requirements.md
│   ├── 5_Domain_Requirements.md
│   ├── 6_User_Stories_and_Acceptance_Criteria.md
│   ├── 7_Product_Backlog_Story_Points_Priority.md
│   ├── 8_Product_Epics.md
│   ├── 9_Sprint_Plan.md
│   └── contributor_feature_report.md
├── Phases/                          # Phase-Wise Project Specifications
│   └── README.md
├── DOCKER_SETUP_GUIDE.md            # Comprehensive Docker & Atlas Setup Guide
├── Dockerfile                       # Multi-stage container specification
├── docker-compose.yml               # Container orchestration configuration
├── requirements.txt                 # Python project dependencies
├── .env.example                     # Environment configuration template
└── README.md                        # Master Project Documentation (This File)
```

---

## 👥 Team Members & Contributions

Developed by **Team OpenTirZ** for the Software Engineering Practicum:

| Member | Engineering Role | Core Contributions |
| :--- | :--- | :--- |
| **Shah Varshil** (`svarshil56`) | **Backend Lead & DevOps Engineer** | System architecture, Docker containerization & Compose orchestration, Data Synchronization Router (`/api/projects/{id}/sync-*`), GitHub Telemetry Ingestion, and deployment pipelines. |
| **Vandit** | **Frontend Lead Developer** | Frontend architecture & user interface design using **React.js** (Authentication UI, Project Management Dashboard, Repository Connection, and Health telemetry views). |
| **Tirth Patel** (`Tirth9978`) | **Database Architect & Backend Engineer** | MongoDB Atlas cluster design, database schema modeling, persistence layer implementation, compound indexing strategy `(projectId, sha)`, and backend code structure. |
| **Ramit** (`ramit7707`) | **Authentication & Security Engineer** | Core JWT authentication system (`/auth/signup`, `/auth/login`, `/auth/me`), password hashing (Bcrypt), stateless session security, and 60+ automated test cases suite. |
| **Shivani Chaudhary** (`shivani`) | **Security & Quality Assurance Engineer** | Enterprise hardening, automated secret masking and token redaction filter in logging, centralized exception handling, and error response sanitization. |
| **Darpan Sherathiya** (`Darpan0610`) | **Backend Engineer (Git Analytics)** | Git commit ingestion pipeline, SHA-level deduplication logic, commit author parsing, and repository branch tracking. |
| **Gaurav Rathod** (`Gaurav Rathod`) | **Backend Engineer (Project Management)** | Project lifecycle CRUD APIs (`/api/projects`), Pydantic schema validation, member ownership enforcement, and project management test suite. |
| **Prince Savaliya** (`Prince Savaliya`) | **Backend Engineer (GitHub Services)** | Contributor retrieval service, GitHub REST API client with pagination & rate-limiting, and contributor-to-project mapping. |
| **Yagnik N.** (`Yagnik N.`) | **Security, RBAC & Agile Process Lead** | Role-Based Access Control (RBAC) implementation, authorization route guards, stakeholder elicitation, user stories, and agile sprint documentation. |

---

## 📜 License & Academic Integrity

This project is submitted for academic evaluation under the Software Engineering Curriculum. All rights reserved by the project authors. Built with industry best practices and clean architecture principles.
