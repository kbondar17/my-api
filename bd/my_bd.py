from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

try:
    from bd.my_postgress import uri
except Exception as ex:
    print(ex)
engine = create_engine(os.getenv('DATABASE_URL',uri)) # echo - логирование sql запросов

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()



