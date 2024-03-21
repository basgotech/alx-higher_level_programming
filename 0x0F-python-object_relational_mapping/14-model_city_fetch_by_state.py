#!/usr/bin/python3
""" Script to print all city names with their state from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create metadata and create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and their corresponding state names
    for i in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(i[0] + ": (" + str(i[1]) + ") " + i[2])
