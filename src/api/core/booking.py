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
    def create_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def get_booking(self, booking_id: int) -> Optional[Booking]:
        pass

    @abstractmethod
    def get_booking_by_id(self, room_id: int) -> List[Booking]:
        pass

    @abstractmethod
    def update_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def delete_booking(self, booking_id: int) -> None:
        pass

# Implementing storage in memory (Реализация хранилища в памяти)
class InMemoryRepository(BookingRepository):
    
    def __init__(self):
        self.bookings = List[Booking] = []

    def create_booking(self, booking: Booking) -> None:
        self.bookings.append(booking)

    def  get_booking(self, booking_id):
        for booking in self.bookings:
            if booking.id == booking_id:
                return booking
            return None
            
    def get_booking_by_id(self, booking_id) -> List[Booking]:
        return [booking for booking in self.bookings if booking_id == booking.id]
    
    def update_booking(self, booking: Booking) -> None:
        for index, existing_booking in enumerate(self.bookings):
            if existing_booking.id == booking.id:
                self.bookings[index] = booking
                return
        raise ValueError(f'Booking ID {booking.id} not found')
    
    def delete_booking(self, booking_id) -> None:
        for index, existing_booking in enumerate(self.bookings):
            if booking_id == existing_booking.id:
                self.bookings.pop(index)
        raise ValueError(f'Booking ID {existing_booking.id} not found')
    


            
        