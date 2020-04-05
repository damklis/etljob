from unittest import mock
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


@mock.patch("etl.loader.azair_content_loader.AZAirContentLoader.load_content")
@mock.patch("sqlalchemy.ext.declarative.declarative_base")
def test_load_content(load_content, base):

    content_stream = generate_content_stream()
    load_content(content_stream)

    assert load_content.called_once_with(content_stream)
