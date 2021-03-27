#!/usr/bin/python3
"""Fetches all states containing the letter 'n'"""
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

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
