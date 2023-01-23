#!/usr/bin/env bash

set -e

curl -sSL https://install.python-poetry.org | python3 -
cd valve_analytics_webapp/
poetry install
poetry run pre-commit install
