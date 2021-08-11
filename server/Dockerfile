FROM python:3.8

ENV PYTHONUNBUFFERED True

RUN pip install Flask gunicorn firebase-admin

COPY src/ app/
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app