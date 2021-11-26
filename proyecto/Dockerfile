FROM python:3.8-alpine

LABEL name="API del clima"
LABEL authors="Alejandro Herrera"
LABEL description="Esta imagen contiene una API que sera consultada para obtener el clima de una ciudad"
COPY ./requirements.txt ./requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev

RUN apk add --no-cache --virtual alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev postgresql-libs


RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir psycopg2 && \
    pip install -r requirements.txt

WORKDIR /opt

COPY . ./

VOLUME ["/config", "/logs"]

CMD [ "python3", "app/main.py" ]
