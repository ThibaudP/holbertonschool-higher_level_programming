#!/usr/bin/python3
"""Inserts a new object in the database"""
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))

    session.close()
