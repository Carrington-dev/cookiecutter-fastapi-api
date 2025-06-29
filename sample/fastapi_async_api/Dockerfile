# FastAPI Async API Dockerfile

FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install poetry && poetry install --no-dev

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
