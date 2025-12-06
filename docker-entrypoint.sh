#!/usr/bin/env sh
set -e

echo "DATABASE_URL: $DATABASE_URL"

echo "Waiting for database to be ready..."

uv run python - << 'PY'
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

url = os.environ.get("DATABASE_URL")
if not url:
    print("ERROR: DATABASE_URL is not set")
    raise SystemExit(1)

engine = create_engine(url)

max_attempts = 30
for attempt in range(1, max_attempts + 1):
    try:
        with engine.connect() as conn:
            print("Database is ready!")
            break
    except OperationalError as e:
        print(f"[Attempt {attempt}/{max_attempts}] Database not ready yet: {e}")
        if attempt == max_attempts:
            print("Failed to connect to database after max attempts, exiting.")
            raise
        time.sleep(2)
PY

echo "Running Alembic migrations..."
uv run alembic upgrade head

echo "Starting application..."
exec "$@"

