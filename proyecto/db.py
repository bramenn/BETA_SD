from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import config


print(config.get("database"))
conn = create_engine("postgresql://beta_sd:lag404@postgres/clima")

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()
