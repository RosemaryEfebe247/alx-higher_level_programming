#!/usr/bin/python3
"""
Importing the modules and the declarative_base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata)


class State(Base):
    """
    Defines each row of the database.
    """
    __tablename__= 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=True)
