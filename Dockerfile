FROM python:3.11.0-slim-buster

WORKDIR /app
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install -r requirements.txt

CMD ["gunicorn", "config.wsgi:application", "-bind", "0.0.0.0:8000"]
