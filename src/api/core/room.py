from dataclasses import dataclass

@dataclass
class Room:
    id: str
    name: str
    capacity: int
    price: int
    hotel_id: str

    def __repr__(self):
        return f'Booking {self.name}, capacity - {self.capacity}, price per night {self.price}'
    
    def __eq__(self, value):
        pass #Реализовать функцию сравнения
