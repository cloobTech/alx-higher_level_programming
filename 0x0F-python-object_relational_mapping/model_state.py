#!/usr/bin/python3
""" contains the class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id: int = Column(Integer, unique=True, primary_key=True, nullable=False)
    name: str = Column(String(128), nullable=False)
