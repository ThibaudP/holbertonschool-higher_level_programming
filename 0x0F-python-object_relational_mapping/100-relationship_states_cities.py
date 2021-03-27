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

    new_state = State(name="California")
    new_state.cities.append(City(name="San Francisco"))
    session.add(new_state)
    session.commit()

    session.close()
