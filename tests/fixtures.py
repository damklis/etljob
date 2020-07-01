import pytest
from pkg_resources import resource_string
from etl.transformer.azair_content_transformer import AZAirContentTransformer
from etl.extractor.azair_content_parser import AZAirContentParser


def generate_content_stream():

    parser = "lxml"
    transformer = AZAirContentTransformer(parser)
    raw_content = resource_string(
        __name__, "test_data/raw_content.txt"
    )
    for flight in transformer.transform_raw_content(raw_content):
        yield flight


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


@pytest.fixture()
def transformer():
    parser = "lxml"
    yield AZAirContentTransformer(parser)


@pytest.fixture()
def example_raw_content():
    yield resource_string(
        __name__,
        "test_data/raw_content.txt"
    )