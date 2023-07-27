from tkinter import CASCADE
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import date

Base = declarative_base()

class Word(Base):
    __tablename__ = 'table_word'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word_name = Column(String(20),nullable=False)
    definition = Column(String(100), nullable=False)
    example = Column(String(100), nullable=False)
    creation_datetime = Column(Date, nullable=False)
    creator_id = Column(Integer, ForeignKey('table_creator.id', ondelete='CASCADE'), nullable=False)
    creator = relationship('Creator', backref='word', lazy='subquery')

    def get_word_definition(self):
        return f'{self.word_name} = {self.definition} | created by {self.creator.get_creator_name()}'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creation_datetime = date.today()


class Creator(Base):
    __tablename__ = 'table_creator'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20),nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)

    def get_creator_name(self):
        return f'{self.first_name} {self.last_name}'
    



