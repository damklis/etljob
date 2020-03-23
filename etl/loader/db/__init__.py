import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = "sqlite:///" + os.path.join(basedir, "db.sqlite3")

engine = create_engine(db_path)

Session = sessionmaker(bind=engine)

Base = declarative_base()


if __name__ == "__main__":
    pass