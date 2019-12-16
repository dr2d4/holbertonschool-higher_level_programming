#!/usr/bin/python3
"""
    Get all States and Citys "objects"
"""

from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'

    engine = create_engine(
        engine.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id)

    for s, c in query:
        print("{}: {} -> {}".format(c.id, c.name, s.name))

    session.close()
