#!/usr/bin/python3
"""
    Definition of the class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
        Class State - Base Sql Alchemy
    """
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'

    def __str__(self):
        """
            Return "id: name" of the object
        """
        return "{}: {}".format(self.id, self.name)
