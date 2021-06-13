import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from etl.config import ETLConfig as cfg



db_path = "sqlite:///" + os.path.join(cfg.DATA_DIR, f"{cfg.DB_NAME}.sqlite3")

engine = create_engine(db_path)

Session = sessionmaker(bind=engine)

Base = declarative_base()
