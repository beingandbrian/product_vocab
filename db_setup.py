# establish db connection like a context manager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from model import *

# context manager for session
@contextmanager
def session_manager():
    # instantiating a session from a Session class
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

engine = create_engine('sqlite:///vocab.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)