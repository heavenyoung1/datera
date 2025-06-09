from datetime import date
from abc import ABC, abstractmethod
from typing import List, Optional

class Booking:
    def __init__(
            self,
            id: str,
            room_id: str,
            check_in: date,
            check_out: date,
    ):
        self.id = id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out

    def __repr__(self):
        return f'Booking {self.room_id}, check in date - {self.check_in}, check out date {self.check_out}'
    
class BookingRepository(ABC):

    @abstractmethod
    def add_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def get_booking(self, booking_id: int) -> Optional[Booking]:
        pass

    @abstractmethod
    def change_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def get_booking_by_id(self, room_id: int) -> List[Booking]:
        pass

    @abstractmethod
    def delete_booking(self, booking_id: int) -> None:
        pass

# Implementing storage in memory (Реализация хранилища в памяти)
class InMemoryRepository(BookingRepository):
    pass