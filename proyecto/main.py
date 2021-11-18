# Este es el archivo principal de todo el programa
# Aqui vamos a definir el servidor de uvicorn
# Este servidor nos permitira hacerle consultas a la api
# Aqui importamos todas las rutas que va encontrar uvicorn
# uvicorn las podra hacer visibles a consultas de cualquier persona (cliente)

from fastapi import FastAPI
import uvicorn

# Se importan todas las rutas
from Clima import rutas as rutas_clima

# Se importan los modelos
from Clima import modelo

# Se importa la configuracion de la bd
import db

# Se crea la aplicacion de FastApi
app = FastAPI()

# Se importan las rutas de la API:

# Ruta de clima
app.include_router(rutas_clima.router , prefix="/v1/clima", tags=["climas"])


# Aqui se corre el programa
if __name__ == "__main__":

    # Corre las migraciones de la bd
    print("Corriendo migraciones de la bd")
    db.Base.metadata.create_all(db.conn)

    #Corre el servidor de uvicorn para la api
    uvicorn.run(app="main:app", )