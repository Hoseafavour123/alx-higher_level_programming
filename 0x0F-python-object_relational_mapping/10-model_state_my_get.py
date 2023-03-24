#!/usr/bin/python3
"""Retrieve state id from state name passed as an argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, States


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query_state = session.query(States)

    found = False

    for state in query_state:
        if state.name == sys.argv[4]:
            print(state.id)
            found = True
            break
    if found is False:
        print("Not found")
