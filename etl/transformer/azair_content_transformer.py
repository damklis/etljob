import uuid
from datetime import date
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import lxml


@dataclass(frozen=True)
class FlightRow:

    uuid: str
    direction: str
    day: str
    flight_date: str
    start: str
    departure: str
    target: str
    arrival: str
    duration: str
    change: str
    price: str
    date: str = str(date.today())

class AZAirContentTransformer:


    def __init__(self, parser):
        self.parser = parser
        self.row_formatter = self.RowFromatter()

    class RowFromatter:

        _routes = ["caption tam", "caption sem"]

        def generate_uuid(self):
            """
            Returns unique flight identification number.
            """
            return str(uuid.uuid4()) 
        
        def extract_results(self, bs_object):
            """
            Returns list of HTML result's class that follow provided name.
            """
            return (
                res for res in bs_object.find_all(class_="result")
            )

        def map_row(self, ptag, _id):
            """
            Returns dictionary with flight data as row.
            """
            day, flight_date = ptag.find("span", "date").text.split(" ")
            _from = ptag.find("span", "from").text.strip()
            ffloor = _from.find(" ")
            departure, start = (_from[:ffloor], _from[ffloor:])
            duration, change = ptag.find("span", "durcha").text.split("/")
            _to = ptag.find("span", "to").text
            arrival, target = (_to[:ffloor], _to[ffloor:])
            direction = ptag.find("span", class_=self._routes).text
            price = ptag.find("span", "subPrice").text.split(" ")[0]

            return FlightRow(
                _id,
                direction,
                day,
                flight_date,
                start.strip(),
                departure,
                target.strip(),
                arrival,
                duration[:5].strip(),
                change.split(" ")[1].replace("no", "0"),
                price
            )

        def extract_ptags(self, result):
            """
            Returns list of tags that follow provided condition.
            """
            return (
                tag for tag in result.find_all("p") 
                if "caption " in str(tag)
            )

        def create_flight_row(self, bs_object):
            """
            Returns JSON object containing detailed information
            about each flight. Every object in data list represents 
            row in database. 
            """
            for result in self.extract_results(bs_object):
                uuid = self.generate_uuid()
                for ptag in self.extract_ptags(result):    
                    yield self.map_row(
                        ptag,
                        uuid
                    )
        

    def transform_raw_content(self, raw_content):

        bs_object = BeautifulSoup(raw_content, self.parser)
        
        return (
            row for row in self.row_formatter.create_flight_row(bs_object)
        )


    

    

