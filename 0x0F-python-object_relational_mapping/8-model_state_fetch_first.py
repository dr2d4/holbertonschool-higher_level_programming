#!/usr/bin/python3
"""
    Get first register "object" of states table
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'

    engine = create_engine(
        engine.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    if state:
        print(state)
    else:
        print('Nothing')

    session.close()
