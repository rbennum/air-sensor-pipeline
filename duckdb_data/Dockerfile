FROM python:3.11.11-slim-bullseye

RUN apt update && apt install -y wget unzip \
    && wget https://github.com/duckdb/duckdb/releases/download/v1.2.0/duckdb_cli-linux-amd64.zip \
    && unzip duckdb_cli-linux-amd64.zip \
    && mv duckdb /usr/local/bin/ \
    && chmod +x /usr/local/bin/duckdb \
    && rm duckdb_cli-linux-amd64.zip

WORKDIR /data

RUN python -m venv .venv \
    && .venv/bin/pip install --upgrade pip \
    && .venv/bin/pip install duckdb kafka-python

CMD ["tail", "-f", "/dev/null"]
