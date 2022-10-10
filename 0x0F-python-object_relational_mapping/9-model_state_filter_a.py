#!/usr/bin/python3
"""This script lists all `State` objects containing the letter `a`.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    states = session.query(State).order_by(State.id).filter(State.name.like
                                                            ('%a%'))
    for state in states:
        print("{}: {}".format(state.id, state.name))
