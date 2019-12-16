#!/usr/bin/python3
"""
    Definition of the class City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
        Class City - Base Sql Alchemy
    """
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = 'cities'

    def __str__(self):
        """
            Return "id: name" of the object
        """
        return '{}: {}'.format(self.id, self.name)
