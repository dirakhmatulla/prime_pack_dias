# ── Stage 1: build wheel ──────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir build

COPY pyproject.toml ./
# Используем команду, которая копирует README, если он есть, и игнорирует, если нет
COPY README.md* ./  
COPY prime_pack_dias/ ./prime_pack_dias/

RUN python -m build --wheel --outdir /dist

# ── Stage 2: lean runtime image ───────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /dist/*.whl /tmp/

RUN pip install --no-cache-dir /tmp/*.whl && rm -rf /tmp/*.whl

ENTRYPOINT ["python", "-m", "prime_pack_dias"]
CMD ["--count", "1000", "--seed", "100"]