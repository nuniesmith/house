# ============================================================================
# FloorPlan Designer — Multi-Stage Dockerfile
# ============================================================================
# Stage 1 (test-builder): Install Python deps, run pytest, generate initial
#                          floor plan outputs to verify everything works.
# Stage 2 (runtime):      Slim Python image with nginx + supervisord to serve
#                          the static HTML front-end and the FastAPI REST API.
# ============================================================================

# ------------------------------------------------------------------
# Stage 1 — Test & Build
# ------------------------------------------------------------------
FROM python:3.12-slim AS builder

WORKDIR /build

# Install system deps needed by matplotlib (non-interactive)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (layer cache optimisation)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code, tests, and config
COPY src/          src/
COPY tests/        tests/
COPY config.yaml   config.yaml
COPY pytest.ini    pytest.ini

# Run the test suite — build fails if tests fail
RUN python -m pytest tests/ -v --tb=short

# Generate initial floor plan outputs to verify the pipeline works
RUN mkdir -p output && \
    python src/main.py --config config.yaml --png-only && \
    echo "✅ PNG generation succeeded"

# ------------------------------------------------------------------
# Stage 2 — Runtime
# ------------------------------------------------------------------
FROM python:3.12-slim AS runtime

LABEL maintainer="jordan"
LABEL description="FloorPlan Designer — nginx + FastAPI"

WORKDIR /app

# Install nginx and supervisord, plus minimal runtime deps for matplotlib
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
    curl \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (runtime only — no dev/test tools)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source from the builder stage
COPY --from=builder /build/src/       /app/src/
COPY --from=builder /build/config.yaml /app/config.yaml

# Copy pre-generated output from the builder stage
COPY --from=builder /build/output/    /app/output/

# Copy static HTML front-end into nginx's document root
COPY src/html/ /usr/share/nginx/html/

# Copy nginx configuration
COPY config/nginx.conf /etc/nginx/conf.d/default.conf

# Remove the default nginx site if it exists
RUN rm -f /etc/nginx/sites-enabled/default

# Create log directories
RUN mkdir -p /var/log/supervisor /var/log/nginx /var/log/floorplan

# ------------------------------------------------------------------
# Supervisord configuration (inline)
# ------------------------------------------------------------------
RUN cat > /etc/supervisor/conf.d/floorplan.conf <<'EOF'
[supervisord]
nodaemon=true
logfile=/var/log/supervisor/supervisord.log
pidfile=/var/run/supervisord.pid
loglevel=info

[program:nginx]
command=nginx -g "daemon off;"
autostart=true
autorestart=true
stdout_logfile=/var/log/nginx/stdout.log
stderr_logfile=/var/log/nginx/stderr.log
priority=10

[program:fastapi]
command=uvicorn src.api:app --host 0.0.0.0 --port 5000
directory=/app
autostart=true
autorestart=true
stdout_logfile=/var/log/floorplan/api-stdout.log
stderr_logfile=/var/log/floorplan/api-stderr.log
environment=CONFIG_PATH="/app/config.yaml",OUTPUT_PATH="/app/output",MPLBACKEND="Agg"
priority=20
EOF

# ------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------
ENV PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg \
    CONFIG_PATH=/app/config.yaml \
    OUTPUT_PATH=/app/output \
    API_PORT=5000

# Expose HTTP port
EXPOSE 80

# Health check — hit the nginx-served page and the API health endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost/ && curl -f http://localhost/api/health || exit 1

# Start both nginx and the FastAPI API via supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/floorplan.conf"]
