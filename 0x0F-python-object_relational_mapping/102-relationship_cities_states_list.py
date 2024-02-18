#!/usr/bin/python3
"""Lists all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for mycity in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(mycity.id, mycity.name, mycity.state.name))
