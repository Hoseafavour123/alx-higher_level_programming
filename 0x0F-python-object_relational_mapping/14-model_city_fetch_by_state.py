#!/usr/bin/python3
"""Print information from database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Cities
from model_state import States


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(Cities, States).filter(Cities.state_id ==\
            States.id).order_by(Cities.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
