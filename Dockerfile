
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

LABEL org.opencontainers.image.authors="Szymon Jagusiak"

WORKDIR /app


COPY --from=builder /root/.local /root/.local
COPY app.py .


ENV PATH=/root/.local/bin:$PATH
ENV PORT=8080


HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/ || exit 1

EXPOSE 8080

FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

LABEL org.opencontainers.image.authors="Szymon Jagusiak"

WORKDIR /app


COPY --from=builder /root/.local /root/.local
COPY app.py .


ENV PATH=/root/.local/bin:$PATH
ENV PORT=8080


HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/ || exit 1

EXPOSE 8080


CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]