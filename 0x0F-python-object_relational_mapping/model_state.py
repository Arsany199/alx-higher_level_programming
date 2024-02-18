#!/usr/bin/python3
"""class definition of a State inherits from sqlalchemy"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """class of state inherits the base"""

    __tablename__ = "states"
    id = colomn(integer, primary_key=True, autoincrement=True, nullable=False)
    name = colomn(string(128), nullable=False)
