from fastapi import APIRouter
from datetime import datetime
from Clima.modelo import search_clima
router = APIRouter()

@router.get("/obtener_clima")
def obtener_clima():
    clima = search_clima()
    clima = {
        "ciudad":clima.ciudad,
        "temperatura": clima.temperatura,
        "timestamp": datetime.fromtimestamp(clima.timestamp)
    }
    return clima