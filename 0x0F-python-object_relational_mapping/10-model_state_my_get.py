#!/usr/bin/python3
"""This script prints the `State` object id with the name passed as argument
from the database `hbtn_0e_6_usa`.
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
    state = session.query(State).filter(State.name == argv[4]).one_or_none()
    if state is None:
        print("Not found")
    else:
        print(state.id)
