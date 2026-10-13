# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Prevent Python from writing pyc files to disc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install system dependencies (curl for container healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir bcrypt "python-jose[cryptography]" email-validator

# Copy project files into container
COPY conftest.py ./
COPY Backend/ ./Backend/

# Expose backend port
EXPOSE 8000

# Container healthcheck using FastAPI health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

# Start the FastAPI application with Uvicorn
CMD ["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
