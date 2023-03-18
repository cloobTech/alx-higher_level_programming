#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # check command line arguments
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <mysql username>"
                " <mysql password> <database name> <statename<>",
            pool_pre_ping=True)
        sys.exit(1)

    # connect to database using SQLAlchemy
    username, password, db_name, state_name = sys.argv[1:]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()

    # query for states that contain letter "a" and print them
    state = db_session.query(State).filter_by(name=state_name).first()
    if not state:
        print("Not found")
    else:
        print(f"{state.id}")
