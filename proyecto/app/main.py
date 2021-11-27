# Este es el archivo principal de todo el programa
# Aqui vamos a definir el servidor de uvicorn
# Este servidor nos permitira hacerle consultas a la api
# Aqui importamos todas las rutas que va encontrar uvicorn
# uvicorn las podra hacer visibles a consultas de cualquier persona (cliente)

import uvicorn
from fastapi import FastAPI
import logging
from fastapi.middleware.cors import CORSMiddleware

from config import config


# Se importan todas las rutas
from Clima import rutas as rutas_clima

# Se importan los modelos
from Clima import modelo

# Se importa la configuracion de la bd
import db

# from config import config
# Se crea la aplicacion de FastApi
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Se importan las rutas de la API:

# Ruta de clima
app.include_router(rutas_clima.router, prefix="/v1/clima", tags=["climas"])


if __name__ == "__main__":
    # db.Base.metadata.create_all(db.conn)
    uvicorn_arg = config.get("allowed_args_for_uvicorn")
    uvicorn.run(app="main:app", **uvicorn_arg)
