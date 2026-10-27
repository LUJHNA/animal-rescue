FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# One worker: SQLite does not like concurrent writers across processes.
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 1 --threads 4 --timeout 60 app:app
