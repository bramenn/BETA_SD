FROM python:3.8-alpine

LABEL name="api-clima"
LABEL authors="Alejandro Herrera"
LABEL description="API para consultar el clima"

RUN apk add --no-cache --virtual alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apk del alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev

WORKDIR /opt

COPY . ./

VOLUME ["/config", "/logs"]

CMD [ "python3", "app/main.py" ]