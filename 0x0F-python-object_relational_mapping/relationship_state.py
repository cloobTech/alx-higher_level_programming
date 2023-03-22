#!/usr/bin/python3
""" contains the class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    __tablename__ = 'states'

    id: int = Column(Integer, unique=True, primary_key=True, nullable=False)
    name: str = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='all, delete')
