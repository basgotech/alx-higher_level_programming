#!/usr/bin/python3
""" Script to generate SQL comment. """

from sqlalchemy import String, MetaData, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

mdata = MetaData()
Base = declarative_base(metadata=mdata)


class State(Base):
    """
    This class represents the 'states' table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
