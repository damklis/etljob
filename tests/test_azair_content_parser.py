import pytest
import requests
from etl.extractor.azair_content_parser import AZAirContentParser


@pytest.fixture()
def azair_parser():
    url = "http://www.azair.com/azfin.php"
    params = {
        "tp" : 0,
        "searchtype" : "flexi"
    }
    yield AZAirContentParser(
        url=url,
        params=params
    )


def test_extract_content(azair_parser):

    expected_bytes = bytes

    result = azair_parser.extract_content()

    assert isinstance(result, expected_bytes)


def test_is_good_response(azair_parser):
    
    url = "http://www.azair.com/"
    bad_url = "http://www.azair.com/poland"
    
    good_response = requests.get(url)
    bad_response = requests.get(bad_url)

    result = azair_parser.is_good_response(good_response)
    result2 = azair_parser.is_good_response(bad_response)

    assert result is True
    assert result2 is False
