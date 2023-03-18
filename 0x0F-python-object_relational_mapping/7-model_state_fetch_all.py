#!/usr/bin/python3
"""
     a script that lists all State objects from
     the database hbtn_0e_6_usa using sqlAlchemy
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # check command line arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # connect to database using SQLAlchemy
    username, password, db_name = sys.argv[1:]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    LocalSession = sessionmaker(bind=engine)
    db = LocalSession()

    # query for all states and print them
    query = db.query(State).order_by(State.id)
    for state in query.all():
        print(f"{state.id}: {state.name}")
