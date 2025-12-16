#!/usr/bin/env bash

set -e
cd /Users/aaronkofihaizel/aaronDev/rcf_consultant
docker compose -f docker-compose.dev.yml down --remove-orphans