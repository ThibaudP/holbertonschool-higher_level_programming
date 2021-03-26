#!/usr/bin/python3
"""Fetches a state that matches a search string"""
from sys import argv
from model_state import Base, State

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

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
