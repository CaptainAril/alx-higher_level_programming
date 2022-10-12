#!/usr/bin/python3
"""This script prints all the `City` objects from the
database `hbtn_0e_14_usa`.
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    cities = session.query(City, State).filter(State.id == City.state_id)\
        .order_by(City.id)
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
