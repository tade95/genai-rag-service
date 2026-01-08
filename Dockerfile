# 🐳 Objetivo del Docker setup:
#  -Imagen liviana
# - No correr como root
# - Configurable por environment
# - Lista para Cloud Run / Kubernetes
# - Compatible con CI/CD

# Base image
FROM python:3.10-slim

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Create non-root user
RUN useradd -m appuser
USER appuser

# Expose port (Cloud Run uses 8080)
EXPOSE 8080

# Start FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# 📝 Frase para el CV / entrevista
# Containerized a FastAPI-based GenAI service using Docker, following production best practices such as non-root execution, environment-based configuration, and cloud-native defaults.