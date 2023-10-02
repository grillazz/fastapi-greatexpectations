FROM python:3.11-slim-bookworm AS base
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends gnupg2 curl \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*


FROM base AS msodbcsql18
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux/installing-the-microsoft-odbc-driver-for-sql-server-on-linux
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
# optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
#RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
#RUN source ~/.bashrc
# optional: for unixODBC development headers
#RUN apt-get install -y unixodbc-dev
# optional: kerberos library for debian-slim distributions
#RUN apt-get install -y libgssapi-krb5-2


FROM msodbcsql18 AS poetry

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && mkdir -p /cache/poetry \
    && poetry config cache-dir /cache/poetry

FROM poetry AS install
WORKDIR /home/code

# allow controlling the poetry installation of dependencies via external args
COPY pyproject.toml poetry.lock ./

# install without virtualenv, since we are inside a container
RUN --mount=type=cache,target=/cache/poetry \
    poetry install --no-root --only main

# cleanup
RUN curl -sSL https://install.python-poetry.org | python3 - --uninstall
RUN apt-get purge -y curl git build-essential \
    && apt-get clean -y \
    && rm -rf /root/.cache \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

FROM install as app-image

ENV PYTHONPATH=/home/code/ PYTHONHASHSEED=0

COPY tests/ tests/
COPY app/ app/
COPY .env logger.ini ./

# create a non-root user and switch to it, for security.
RUN addgroup --system --gid 1001 "app-user"
RUN adduser --system --uid 1001 "app-user"
USER "app-user"

