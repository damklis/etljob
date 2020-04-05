from dataclasses import asdict
from etl.loader.chunk_generator import generate_chunk
from etl.loader.db import (
    engine, Session, Base, Flight
)


class AZAirContentLoader:

    def __init__(self, chunk_size=10):
        self.chunk_size = chunk_size
        self.session = Session()

    def load_content(self, content):

        for chunk in generate_chunk(content, self.chunk_size):
            
            objects = [Flight(**asdict(row)) for row in chunk]
            self.session.bulk_save_objects(objects)
            self.session.commit()
        
        self.session.close()
