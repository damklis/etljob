from itertools import islice
from dataclasses import asdict
from etl.loader.db import (engine, Session, Base, Flight)


class AZAirContentLoader:

    def __init__(self, chunk_size):
        self.session = Session()
        self.chunk_size = chunk_size

    def load_content(self, content):

        for chunk in generate_chunk(content, self.chunk_size):
            
            objects = [Flight(**asdict(row)) for row in chunk]
            self.session.bulk_save_objects(objects)
            self.session.commit()
        
        self.session.close()


def generate_chunk(content, chunk_size=10):
    
    iterable_content = iter(content)
    while True:
        batch = list(islice(iterable_content, chunk_size))
        if not batch:
            return
        yield batch