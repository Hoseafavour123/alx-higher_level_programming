#!/usr/bin/python3
"""Update a states object from hbtn_0e_6_usa"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, States
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(States).order_by(States.id)
    for state in states:
        if state.id == 2:
            state.name = 'New Mexico'
        print("{}: {}".format(state.id, state.name))
    session.commit()
