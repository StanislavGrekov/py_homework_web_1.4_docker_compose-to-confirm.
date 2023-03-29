FROM python:3.8.6-alpine

MAINTAINER GrekovStas

RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY . ./app
WORKDIR /app
RUN chmod +x script.sh
RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ./script.sh