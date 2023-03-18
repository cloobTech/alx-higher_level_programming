#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    # Create session
    LocalSession = sessionmaker(bind=engine)
    db_session = LocalSession()

    states = db_session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in states:
        print(f'{state.name}: ({city.id}) {city.name}')
