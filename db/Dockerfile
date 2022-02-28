# pull official base image
FROM postgres:13-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

WORKDIR /home/gx/code

COPY shakespeare.sql /home/gx/code/shakespeare.sql

