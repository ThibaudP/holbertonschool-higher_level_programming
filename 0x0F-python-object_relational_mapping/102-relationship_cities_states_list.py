#!/usr/bin/python3
"""Lists all cities by state"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City

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

    # states = session.query(State).order_by(State.id)

    # for state in states:
    #     print("{}: {}".format(state.id, state.name))
    #     for city in state.cities:
    #         print("    {}: {}".format(city.id, city.name))

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
