# ── Stage 1: build wheel ──────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir build

COPY pyproject.toml README.md ./
COPY prime_pack_dias/ ./prime_pack_dias/

RUN python -m build --wheel --outdir /dist

# ── Stage 2: lean runtime image ───────────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /dist/*.whl /tmp/

RUN pip install --no-cache-dir /tmp/*.whl && rm -rf /tmp/*.whl

# All arguments after the image name in `docker run <image> ...` go to the module
ENTRYPOINT ["python", "-m", "prime_pack_dias"]

# Sensible defaults matching the assignment
CMD ["--count", "1000", "--seed", "100"]
