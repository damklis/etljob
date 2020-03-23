import re
from contextlib import closing
from requests import get
from requests.exceptions import ConnectionError, HTTPError


class AZAirContentParser:

    def __init__(self, url, params):
        self.url = url
        self.params = params

    def extract_content(self):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(self.url, self.params, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except ConnectionError as con_err:
            print(f"Connection error occurred. More info: {con_err}.")

        except HTTPError as http_err:
            print(f"HTTP error occurred. More info: {http_err}.")

    @staticmethod
    def is_good_response(response):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = response.headers['Content-Type'].lower()
        return (
            response.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1
        )

    def __str__(self):
        clean_link = re.sub("(http[s]?://|www.)", "", self.url)
        domain, _ = clean_link.split(".")
        return f'WebContentParser of {domain.upper()}'
