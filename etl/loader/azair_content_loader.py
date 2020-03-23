from dataclasses import asdict
from etl.loader.db.flight import Flight
from etl.loader.db.base import (
    Session, engine, Base
)


Base.metadata.create_all(engine)


class AZAirContentLoader:

    def __init__(self):
        self.session = Session()


    def load_content(self, rows):
        for row in rows:
            self.session.add(
                Flight(
                    **asdict(row)
                )
            )
            self.session.commit()