#!/usr/bin/python3
"""This script changes the name of a `State` object from the database
`hbtn_0e_6_usa`.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.commit()
