import db
from sqlalchemy import Column, Integer, String
from random import randint
class Clima(db.Base):
    """Este modelo define los atributos de la tabla clima y sus tipos de dato"""
    __tablename__ = "clima"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column("ciudad", String(255), unique=True, index=True)
    temperatura = Column("temperatura", Integer)
    timestamp = Column("timestamp", Integer)

def search_clima():
    climas = db.session.query(Clima).all()
    clima_int = randint(0, len(climas)-1)
    return climas[clima_int]
