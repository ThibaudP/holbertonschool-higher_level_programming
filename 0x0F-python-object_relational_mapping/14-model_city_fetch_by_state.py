#!/usr/bin/python3
"""Lists all cities by state"""
from sys import argv
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)

    Session = sessionmaker(bind=eng)
    session = Session()

    data = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)

    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
