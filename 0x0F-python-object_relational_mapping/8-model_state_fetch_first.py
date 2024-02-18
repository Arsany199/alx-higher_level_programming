#!/usr/bin/python3
"""script that prints the first State object from the database"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    f_state = session.query(state).order_by(state.id).first()
    if f_state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
