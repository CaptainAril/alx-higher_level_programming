#!/usr/bin/python3
"""Contains the class definition of a `City`
and an instance for `declarative_base`."""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Defines a class City that inherits from Base."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
