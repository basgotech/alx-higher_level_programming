#!/usr/bin/python3
"""
Script to add a new State and City to the database.
"""
import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """ Create a new State object """
    newState = State(name='California')

    """ Create a new City object """
    newCity = City(name='San Francisco')

    """ Add the new City to the State's cities relationship """
    newState.cities.append(newCity)
    
    """ Add the new State and City to the session """
    session.add(newState)
    session.add(newCity)

    """ Commit the changes to the database """
    session.commit()
