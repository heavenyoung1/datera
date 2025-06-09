from typing import List
from room import Room

class Hotel:
    def __init__(
            self,
            id: str,
            name: str,
            rooms: List[Room]
    ):
        self.id = id,
        self.name = name,
        self.rooms = rooms,

    def __repr__(self):
        return f'Booking {self.room_id}, check in date - {self.check_in}, check out date {self.check_out}'