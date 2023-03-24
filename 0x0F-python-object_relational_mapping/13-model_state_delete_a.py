#!/usr/bin/python3
"""Delete states from database that contains letter 'a'"""
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

    states = session.query(States).order_by(States.id)

    for state in states:
        if 'a' in state.name:
            session.delete(state)
        else:
            print("{}: {}".format(state.id, state.name))

    session.commit()
