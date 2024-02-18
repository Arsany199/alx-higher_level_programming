#!/usr/bin/python3
"""changes the name of a State object from the database"""
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

    new_state = session.query(state).fillter_by(id=2).first()
    new_state.name = "New Mexico"
    session.commit()
    session.close()
