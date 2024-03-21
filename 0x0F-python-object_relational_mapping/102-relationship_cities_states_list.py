#!/usr/bin/python3
""" 
Script to list all State objects and 
their corresponding City objects.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

if __name__ == "__main__":
    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create all tables defined in the models
    Base.metadata.create_all(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects ordered by their ID
    for i in session.query(State).order_by(State.id):
        # Print each City object associated with the State
        for ci in i.cities:
            print(ci.id, ci.name, sep=": ", end="")
            print(" -> " + i.name)
