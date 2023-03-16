FROM python:3.11-slim-buster AS base
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl git build-essential \
    && apt-get autoremove -y
ENV POETRY_HOME="/opt/poetry"
#    PIP_DEFAULT_TIMEOUT=100 \
#    PIP_DISABLE_PIP_VERSION_CHECK=1 \
#    PIP_NO_CACHE_DIR=1 \
#    PYTHONDONTWRITEBYTECODE=1 \
#    PYTHONUNBUFFERED=1 \
#    PYTHONFAULTHANDLER=1 \
#    PYTHONHASHSEED=random \
#    LANG=C.UTF-8 \
#    LC_ALL=C.UTF-8

RUN curl -sSL https://install.python-poetry.org | python3 -

FROM base AS install
WORKDIR /app/

# allow controlling the poetry installation of dependencies via external args
ENV POETRY_HOME="/opt/poetry"
ARG POETRY_INSTALL_ARGS="--only main"
ENV PATH="$POETRY_HOME/bin:$PATH"
COPY pyproject.toml poetry.lock ./

# install without virtualenv, since we are inside a container
RUN poetry install $POETRY_INSTALL_ARGS

# cleanup
RUN curl -sSL https://install.python-poetry.org | python3 - --uninstall
RUN apt-get purge -y curl git build-essential \
    && apt-get clean -y \
    && rm -rf /root/.cache \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

FROM install as app-image
COPY app app
COPY .env /app

# create a non-root user and switch to it, for security.
RUN addgroup --system --gid 1001 "app-user"
RUN adduser --system --uid 1001 "app-user"
USER "app-user"
