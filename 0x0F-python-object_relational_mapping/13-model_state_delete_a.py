#!/usr/bin/python3
"""Script that deletes all State objects with a name containing"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State):
        if "a" in i.name:
            session.delete(i)
    session.commit()
    session.close()
