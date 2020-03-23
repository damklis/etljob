from dataclasses import asdict
from etl.loader.db import (
    engine,
    Session,
    Base,
    Flight
)


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
        self.session.close()
