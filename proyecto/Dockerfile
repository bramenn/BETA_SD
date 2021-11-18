FROM python:3.8-alpine

LABEL name="api-clima"
LABEL authors="Alejandro Herrera"
LABEL description="API para consultar el clima"

WORKDIR /opt

COPY . ./

VOLUME ["/config", "/logs"]

RUN apk add --no-cache --virtual alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk del alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev

CMD [ "python3", "main.py" ]
