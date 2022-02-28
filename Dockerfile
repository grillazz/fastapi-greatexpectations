# Pull base image
FROM python:3.10-slim-buster as builder

# Set environment variables
WORKDIR /pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# Install pipenv
RUN set -ex && pip install pipenv --upgrade

# Install dependencies
RUN set -ex && pipenv lock -r > req.txt && pip install -r req.txt

FROM builder as final
WORKDIR /app
COPY ./app/ /app/
COPY .env /app/
