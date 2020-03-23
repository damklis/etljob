from etl.loader.db.flight import Flight
from etl.loader.db.base import (
    engine, Session, Base
)


Base.metadata.create_all(engine)