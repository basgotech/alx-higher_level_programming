#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the provided name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Check if state is found
    if state:
        # Print the state's ID
        print(state.id)
    else:
        # If state is not found, print "Not found"
        print("Not found")

    # Close the session
    session.close()
