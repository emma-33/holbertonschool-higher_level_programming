#!/usr/bin/python3
"""Prints the State object with the name passed as argument
"""
from os import name
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    if new_state is not None:
        print("{}".format(new_state.id))

    session.close()
