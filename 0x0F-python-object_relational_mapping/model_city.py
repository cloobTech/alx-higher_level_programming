#!/usr/bin/python3
""" contains the class definition of a State """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    __tablename__ = 'cities'

    id: int = Column(Integer, unique=True, primary_key=True, nullable=False)
    name: str = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('state.id'), nullable=False, unique=True )
