FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /valve_analytics_webapp

COPY ./pyproject.toml .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .
