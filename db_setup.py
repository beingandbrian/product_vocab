# establish db connection like a context manager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *

# Below generates our db schema
engine = create_engine('sqlite:///vocab.db', echo=True, future=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)