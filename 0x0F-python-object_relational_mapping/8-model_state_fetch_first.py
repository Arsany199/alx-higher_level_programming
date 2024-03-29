#!/usr/bin/python3
"""script that prints the first State object from the database"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    f_state = session.query(State).order_by(State.id).first()
    if f_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(f_state.id, f_state.name))
