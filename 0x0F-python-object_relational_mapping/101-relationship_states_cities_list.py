#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects and their corresponding City objects
    result = session.query(State).order_by(State.id).all()

    # Print out the results
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

