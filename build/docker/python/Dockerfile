FROM python:3.9

# Install distribution deps
RUN apt-get update && \
    apt-get install -y gosu ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY docker/ca-certificates/* /usr/local/share/ca-certificates/
RUN chmod 644 /usr/local/share/ca-certificates/* \
	&& update-ca-certificates --fresh
ENV REQUESTS_CA_BUNDLE "/etc/ssl/certs/ca-certificates.crt"

# Install python deps
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

# Set Workdir
WORKDIR /app