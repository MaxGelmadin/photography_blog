FROM python:bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm

COPY . /code