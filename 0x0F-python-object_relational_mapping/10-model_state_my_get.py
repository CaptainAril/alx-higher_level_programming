#!/usr/bin/python3
"""Prints the `State` object with the name passed as argument
from the database."""

from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == '{}'.format(argv[4]))\
        .all()
    if states:
        for state in states:
            print(state.id)
    else:
        print('Not found')
