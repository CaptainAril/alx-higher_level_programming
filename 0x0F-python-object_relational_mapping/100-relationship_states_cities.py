#!/usr/bin/python3
"""Creates a State and City entry in the database"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                                argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # creates/persists tables in the database from class
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco', state=newState)
    session.add(newState, newCity)
    session.commit()
    session.close()
