# KiranAI Minimal Container Image
FROM python:3.11-slim

LABEL maintainer="S Kiran"
LABEL description="KiranAI: Compact, open-weight AI system under 50 MB"
LABEL org.opencontainers.image.source="https://github.com/skiran"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .
COPY kiran_ai/ ./kiran_ai/
COPY tests/ ./tests/
COPY plan.md .

# Install package
RUN pip install --no-cache-dir .

# Default entrypoint runs KiranAI CLI
ENTRYPOINT ["kiran"]
CMD ["run"]

