#!/usr/bin/python3
"""
    Create new State 'object'
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

    louisiana_state = State(name='Louisiana')
    session.add(louisiana_state)
    session.commit()

    print(louisiana_state.id)
    session.close()
