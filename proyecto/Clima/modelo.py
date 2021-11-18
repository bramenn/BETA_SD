import db
from sqlalchemy import Column, Integer, Boolean, String

class Votante(db.Base):
    """Este modelo define los atributos de la tabla votante y sus tipos de dato"""
    __tablename__ = "votante"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column("ciudad", String(255), unique=True, index=True)
    temperatura = Column("temperatura", Integer)
    timestamp = Column("timestamp", Integer)