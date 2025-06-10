from dataclasses import dataclass
from typing import List

from src.api.core.room import Room

@dataclass
class Hotel:
    id: str
    name: str
    city: str
    address: str
    metro_stations: List[str]
    rooms: List[Room]

    def __repr__(self):
        return f'Hotel with ID {self.id}, {self.id}, name - {self.name}, rooms {self.rooms}'