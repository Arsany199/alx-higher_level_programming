#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    mystate = session.query(State).filter(State.name == argv[4]).first()

    insert_state = State(name="Louisiana")
    session.add(insert_state)
    session.commit()
    print(insert_state.id)
    session.close()
