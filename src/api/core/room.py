from dataclasses import dataclass

@dataclass
class Room:
    id: str
    type: tuple
    max_guests: int
    floor: int
    price: int
    hotel_id: str