from dataclasses import dataclass

@dataclass
class Hotel:
    id: str
    name: str
    rooms: int

    def __repr__(self):
        return f'Hotel with ID {self.id}, {self.id}, name - {self.name}, rooms {self.rooms}'