#!/usr/bin/python3
"""class definition of a State inherits from sqlalchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class of state inherits the base"""

    __tablename__ = "states"
    id = column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)
