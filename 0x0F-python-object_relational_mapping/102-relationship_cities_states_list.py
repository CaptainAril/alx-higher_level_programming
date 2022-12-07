#!/usr/bin/python3
"""Lists all City objects, and their corresponding State objects,
contained in the database."""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                                argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).join(State).order_by(City.id)
    for city in cities:
        print("{}: {} -> {}".format(
            city.id, city.name, city.state.name))
