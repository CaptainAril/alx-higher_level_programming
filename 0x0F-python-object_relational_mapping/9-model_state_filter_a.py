#!/usr/bin/python3
"""Prints the all `State` objects from a database containing the letter `a`.
"""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id.asc())
    for state in states:
        print('{}: {}'.format(state.id, state.name))
