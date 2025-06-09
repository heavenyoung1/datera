from dataclasses import dataclass

@dataclass
class Hotel:
    id: str
    name: str
    rooms: int

    def __repr__(self):
        return f'Booking {self.room_id}, check in date - {self.check_in}, check out date {self.check_out}'