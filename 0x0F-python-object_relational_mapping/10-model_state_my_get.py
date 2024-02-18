#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    Base.metadata.create_all(engine)

    my_state = session.query(state).filter(state.name == argv[4]).first()

    if my_state:
        print("{}".format(my_state.id))
    else:
        print("Not found")
    session.close()
