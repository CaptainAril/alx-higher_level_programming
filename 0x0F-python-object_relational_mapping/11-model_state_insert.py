#!/usr/bin/python3
"""This script print the `State` object with the `name` passed as argument
from the database `hbtn_0e_6_usa`.
"""


from sys import argv
from unicodedata import name
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                       .format(argv[1], argv[2], argv[3]))
new_state = State(name='Louisiana')

session_maker = sessionmaker(bind=engine)
session = session_maker()
session.add(new_state)

state = session.query(State).filter(State.name == new_state.name)
for state in state:
    print(state.id)
