#!/usr/bin/python3
"""This module defines a class `City` which inherits from
instance `Base = declarative_base()`.
"""


from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """Represents a class City which inherits from `Base`.
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
