#!/usr/bin/python3

"""
Defines a State class and a Base instance for SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create the Base instance
Base = declarative_base()


class State(Base):
    """State class for the states table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
