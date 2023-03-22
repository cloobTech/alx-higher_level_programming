#!/usr/bin/python3
""" contains the class definition of a State """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'

    id: int = Column(Integer, unique=True, primary_key=True, nullable=False)
    name: str = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'), nullable=False, unique=True )
