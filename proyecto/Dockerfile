FROM python:3.8-alpine

LABEL name="API del clima"
LABEL authors="Alejandro Herrera"
LABEL description="Esta imagen contiene una API que sera consultada para obtener el clima de una ciudad"

RUN apk add --no-cache --virtual alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev postgresql-libs
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apk del alpine-sdk autoconf automake libtool gcc g++ make libffi-dev openssl-dev postgresql-dev postgresql-libs
WORKDIR /opt

COPY . ./

VOLUME ["/config", "/logs"]

CMD [ "python3", "app/main.py" ]
