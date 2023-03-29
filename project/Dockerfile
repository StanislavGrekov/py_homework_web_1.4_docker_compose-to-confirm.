FROM python:3.8.6-alpine

MAINTAINER GrekovStas

WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 8000
