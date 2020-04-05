from pkg_resources import resource_string
import pytest
from etl.loader.chunk_generator import generate_chunk
from etl.transformer.azair_content_transformer import AZAirContentTransformer


def generate_content_stream():

    parser = "lxml"
    transformer = AZAirContentTransformer(parser)
    raw_content = resource_string(
        __name__, "test_data/raw_content.txt"
    )
    for flight in transformer.transform_raw_content(raw_content):
        yield flight 


def test_generate_chunk():

    expected = 2
    
    content_stream = generate_content_stream()
    chunks = generate_chunk(content_stream, chunk_size=2)
    result = len(next(chunks))
    
    assert result == expected
