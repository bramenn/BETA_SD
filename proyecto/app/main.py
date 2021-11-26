# Este es el archivo principal de todo el programa
# Aqui vamos a definir el servidor de uvicorn
# Este servidor nos permitira hacerle consultas a la api
# Aqui importamos todas las rutas que va encontrar uvicorn
# uvicorn las podra hacer visibles a consultas de cualquier persona (cliente)

import uvicorn
from fastapi import FastAPI
import logging

logger = logging.getLogger()

# Se importan todas las rutas
from Clima import rutas as rutas_clima

# Se importan los modelos
from Clima import modelo

# Se importa la configuracion de la bd
from db import get_db
# from config import config
# Se crea la aplicacion de FastApi
app = FastAPI()

# Se importan las rutas de la API:

# Ruta de clima
app.include_router(rutas_clima.router , prefix="/v1/clima", tags=["climas"])


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)