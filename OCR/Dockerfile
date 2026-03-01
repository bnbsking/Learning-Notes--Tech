FROM python:3.12-slim

ENV PATH="/root/.local/bin:$PATH"
ENV PIP_DEFAULT_TIMEOUT=86400

RUN apt update && apt install -y libgl1 libglib2.0-0 poppler-utils curl procps

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY . /app

RUN poetry install --no-root --no-interaction --no-ansi
