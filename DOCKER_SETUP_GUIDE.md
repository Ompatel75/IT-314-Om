# Docker Setup & Execution Guide (MongoDB Atlas)

This guide explains how to set up and run the **AI Software Project Health & Risk Analyzer** using Docker with **MongoDB Atlas** as the centralized cloud database.

---

## 1. Prerequisites

1. **Docker & Docker Compose**:
   - Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running on your system.
2. **MongoDB Atlas Account & Cluster**:
   - You need access to the shared project cluster on MongoDB Atlas.

---

## 2. MongoDB Atlas Configuration Checklist

Before starting the Docker container, ensure the following settings are configured in your **MongoDB Atlas Dashboard**:

### A. Network Access (IP Whitelist)
Because Docker containers run in an isolated bridge network, your Atlas cluster must accept connections from your machine:
1. In MongoDB Atlas, go to **Network Access** (under *Security* on the left panel).
2. Click **Add IP Address**.
3. Choose either **Add Current IP Address** or add `0.0.0.0/0` (Allow Access from Anywhere) for seamless team development.

### B. Database User Access
1. Go to **Database Access** (under *Security*).
2. Ensure your user (e.g. `202401202_db_user`) is created with **Read and write to any database** (or specific rights to `project_health`).
3. If unsure about the password, click **Edit** and set/verify the password.

---

## 3. Environment Configuration (`.env`)

Create a `.env` file in the project root (never commit this file to git):

```env
# MongoDB Atlas connection string
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>.mongodb.net/?retryWrites=true&w=majority
MONGO_DATABASE=project_health

# Auth / JWT configuration
JWT_SECRET_KEY=your-secure-random-secret-key-at-least-32-chars
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# GitHub API personal access token
GITHUB_TOKEN=your_github_personal_access_token
```

> **Tip**: Avoid wrapping the connection string in extra quotes inside `.env`.

---

## 4. How to Run the Application

From the project root directory, run:

```bash
docker compose up
```

To run in the background (detached mode):
```bash
docker compose up -d
```

To rebuild the image after updating dependencies:
```bash
docker compose up --build
```

---

## 5. Verifying the Application

Once running, access the services in your browser:

- **Swagger API Docs (Interactive)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check Endpoint**: [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

## 6. Running Tests Inside Docker

The test suite runs against mocked database operations and does not modify real data in your Atlas cluster:

```bash
docker compose run --rm backend pytest -v
```

To run specific test modules:
```bash
docker compose run --rm backend pytest Backend/auth/test_auth.py -v
docker compose run --rm backend pytest Backend/test_contributor_service.py -v
```

---

## 7. Useful Docker Commands

| Action | Command |
| :--- | :--- |
| **Start backend** | `docker compose up` |
| **Start in background** | `docker compose up -d` |
| **View live logs** | `docker compose logs -f backend` |
| **Stop application** | `docker compose down` |
| **Run tests** | `docker compose run --rm backend pytest -v` |
| **Open container shell** | `docker compose exec backend bash` |
