from pkg_resources import resource_string
import pytest
from etl.loader.chunk_generator import generate_chunk
from etl.transformer.azair_content_transformer import AZAirContentTransformer

from .fixtures import generate_content_stream


def test_generate_chunk():

    expected = 2
    
    content_stream = generate_content_stream()
    chunks = generate_chunk(content_stream, chunk_size=2)
    result = len(next(chunks))
    
    assert result == expected
