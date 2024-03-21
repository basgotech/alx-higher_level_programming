#!/usr/bin/python3
"""
Script to list all State objects containing the 
letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Create engine to connect to MySQL database """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """ Create session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query State objects containing the letter 'a' and order by ID """
    swa = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    """ Check if any states with 'a' were found """
    if swa:
        """ Print the results """
        for st in swa:
            print("{}: {}".format(st.id, st.name))
    else:
        """ If no states with 'a' were found, print 'Nothing' """
        print("Nothing")

    """ Close the session """
    session.close()
