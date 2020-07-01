from datetime import date
from dataclasses import asdict
from pkg_resources import resource_string
import pytest
import requests
from etl.transformer.azair_content_transformer import (
    AZAirContentTransformer, FlightRow
)

from .fixtures import transformer, example_raw_content


def test_raw_content_type(transformer, example_raw_content):

    expected = FlightRow

    content = transformer.transform_raw_content(example_raw_content)
    result = next(content)

    assert isinstance(result, expected)


def test_raw_content_keys(transformer, example_raw_content):
    
    expected = [
        "uuid", "direction", "day", "flight_date", "start",
        "departure", "target","arrival", "duration",
        "change", "price", "date"
    ]

    content = transformer.transform_raw_content(example_raw_content)
    result = [key for key in asdict(next(content)).keys()]

    assert set(result) == set(expected)


def test_raw_content_date(transformer, example_raw_content):

    expected = str(date.today())

    content = transformer.transform_raw_content(example_raw_content)
    result = asdict(next(content)).get("date")

    assert result == expected
