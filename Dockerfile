FROM python:3.10-slim as base
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev
COPY . .
EXPOSE 8000
CMD ["python", "scripts/serve.py"]
