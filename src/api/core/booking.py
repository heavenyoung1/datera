from dataclasses import dataclass
from pendulum import date

@dataclass
class Booking:
    id: str
    hotel_id: str
    room_id: str
    guest_count: int
    check_in: date
    check_out: date