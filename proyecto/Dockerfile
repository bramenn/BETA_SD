# CREAMOS ESTE CONTENEDOR BASADOS EN LA IMAGEM ...
FROM python:3.8-alpine

# DEFINIMOS INFORMACIÓN PARA ESTA IMAGEN
LABEL name="API del clima"
LABEL authors="Alejandro Herrera"
LABEL description="Esta imagen contiene una API que sera consultada para obtener el clima de una ciudad"

# COPIAMOS LOS REQUERIMIENTOS DENTRO DE LA PRIMER CAPA DE ESTE CONTENDERO
COPY ./requirements.txt ./requirements.txt

# INSTALAMOS LOS ERRAMIENTAS NECESARIAS PARA ALPINE
RUN apk add --no-cache --virtual .build-deps \
    python3-dev \
    postgresql-dev \
    libtool \
    g++ \
    postgresql-libs

# INSTALAMOS LOS REQUERIMIENTOS Y ELIMINAMOS LAS HERRAMIENTAS NO NECESARIAS
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install --no-cache-dir psycopg2 && \
    pip install -r requirements.txt && \
    apk del \
    python3-dev \
    postgresql-dev \
    libtool \
    g++ \
    postgresql-libs

# DEFINIMOS QUE LA CARPETA DE TRABAJO ES /opt
WORKDIR /opt
# COPIAMOS TODOS ARCHIVOS DEL PROYECTO EN EL CONTENEDOR
COPY . ./

# CREAMOS EL VOLUMEN PARA EL CONFIG Y PARA LOS LOGS
VOLUME ["/config", "/logs"]

# CORREMOS EL PROYECTO
CMD [ "python", "app/main.py" ]
