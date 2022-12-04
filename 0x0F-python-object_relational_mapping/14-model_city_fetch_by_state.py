#!/usr/bin/python3
"""Prints all City objects from the database."""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id.asc())
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
