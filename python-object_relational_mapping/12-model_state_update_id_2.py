#!/usr/bin/python3
"""Update the State object with the name passed as argument
"""
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

    updated_state = session.query(State).filter(State.id == 2).first()

    if updated_state is not None:
        updated_state.name = 'New Mexico'
        session.commit()

    session.close()
