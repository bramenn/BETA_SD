import db
from sqlalchemy import Column, Integer, String

class Clima(db.Base):
    """Este modelo define los atributos de la tabla clima y sus tipos de dato"""
    __tablename__ = "clima"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column("ciudad", String(255), unique=True, index=True)
    temperatura = Column("temperatura", Integer)
    timestamp = Column("timestamp", Integer)