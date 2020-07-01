from unittest import mock
import pytest
from etl.loader.chunk_generator import generate_chunk

from .fixtures import generate_content_stream


@mock.patch("etl.loader.azair_content_loader.AZAirContentLoader.load_content")
@mock.patch("sqlalchemy.ext.declarative.declarative_base")
def test_load_content(load_content, base):

    content_stream = generate_content_stream()
    load_content(content_stream)

    assert load_content.called_once_with(content_stream)
