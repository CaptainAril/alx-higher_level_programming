#!/usr/bin/python3
"""This module defines a class `state` and an
instance `Base = declarative_base()`.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """Represents a class State which inherits from `Base`.
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
