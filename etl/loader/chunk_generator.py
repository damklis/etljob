from itertools import islice


def generate_chunk(content, chunk_size):
    
    iterable_content = iter(content)
    while True:
        batch = list(islice(iterable_content, chunk_size))
        if not batch:
            return
        yield batch
