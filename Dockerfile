# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Helpful envs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps for psycopg / builds
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv (package manager)
RUN pip install uv

# Install Python deps using uv
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev

# Copy app source
COPY . .

# Entrypoint will:
#  1. wait for DB
#  2. run alembic upgrade head
#  3. start uvicorn
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Default command (overridable from compose)
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
