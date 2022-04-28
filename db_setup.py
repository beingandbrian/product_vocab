# establish db connection like a context manager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine('sqlite:///vocab.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)