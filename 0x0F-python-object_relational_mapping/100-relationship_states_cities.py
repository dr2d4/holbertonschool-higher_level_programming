#!/usr/bin/python3
"""
    Create City 'object'
"""

from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
import sys


if __name__ == '__main__':
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'

    engine = create_engine(engine.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california_state = State(name='California')
    session.add(california_state)
    session.commit()

    california_citie = City(name='San Francisco', state_id=california_state.id)
    session.add(california_citie)
    session.commit()
    session.close()
