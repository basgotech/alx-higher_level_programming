#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.
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
    Session = sessionmaker(bind=c_eng)
    session = Session()

    """ Query the first State object """
    fs_query = session.query(State).order_by(State.id).first()

    """ Check if the first state exists """
    if fs_query:
        print("{}: {}".format(fs_query.id, fs_query.name))
    else:
        print("Nothing")

    """ Close the session """
    session.close()
