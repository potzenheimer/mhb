FROM python:3.9

# Install distribution deps
RUN apt-get update && \
    apt-get install -y gosu ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install python deps
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

# Set Workdir
WORKDIR /app