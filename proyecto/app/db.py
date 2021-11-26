from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

logger = logging.getLogger()

from config import config

conn = create_engine(config.get("database"))

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()
