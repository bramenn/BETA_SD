from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/obtener_clima")
def obtener_clima():
    clima = {
        "ciudad": "Pereira",
        "temperatura": "12", # en grados c
        "timestamp": "1225093",
    }
    return clima