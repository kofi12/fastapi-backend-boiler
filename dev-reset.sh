#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

docker compose -f docker-compose.dev.yml down -v --remove-orphans
docker compose -f docker-compose.dev.yml up -d --build
docker compose -f docker-compose.dev.yml run --rm api \
  uv run python -m app.db.seed
