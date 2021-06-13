from sqlalchemy import (
    Column, String, Integer
)
from etl.loader.db.base import Base


class Flight(Base):

    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    uuid = Column(String)
    direction = Column(String)
    day = Column(String)
    flight_date = Column(String)
    start = Column(String)
    departure = Column(String)
    target = Column(String)
    arrival = Column(String)
    duration = Column(String)
    change = Column(Integer)
    price = Column(String)
    created_at = Column(String)

    def __init__(
            self, uuid, direction, day, flight_date, start,
            departure, target, arrival, duration, change, price, created_at):
        self.uuid = uuid
        self.direction = direction
        self.flight_date = flight_date
        self.day = day
        self.start = start
        self.departure = departure
        self.target = target
        self.arrival = arrival
        self.duration = duration
        self.change = change
        self.price = price
        self.created_at = created_at

    def __str__(self):
        return f"Flight from {self.start} to {self.direction}."
