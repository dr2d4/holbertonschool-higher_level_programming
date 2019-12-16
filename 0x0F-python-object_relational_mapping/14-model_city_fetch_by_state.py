#!/usr/bin/python3
"""
    Displays State (State.id) City
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'

    engine = create_engine(engine.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    for s, c in rows:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))

    session.close()
