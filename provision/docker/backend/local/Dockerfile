FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    POETRY_CACHE_DIR=/data/pypoetry \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1


RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    mkdir -p /srv/http /data/pypoetry && \
    pip install --upgrade pip poetry

COPY entrypoint.sh /srv/entrypoint.sh

RUN chmod 755 /srv/entrypoint.sh /data/pypoetry/

WORKDIR /srv/http

ENTRYPOINT [ "/srv/entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "0:8080"]
