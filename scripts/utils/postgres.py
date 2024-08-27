from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'root'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'movie_db'

# Create the SQLAlchemy engine
DATABASE_URL = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)

if database_exists(engine.url):
    Base = declarative_base()
else:
    create_database(engine.url)
    Base = declarative_base()


class MovieCollection(Base):
    __tablename__ = 'movie_collection'

    name = Column(String, primary_key=True)
    date = Column(String)
    time = Column(String)


Base.metadata.create_all(engine)
