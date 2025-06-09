from datetime import date
from abc import ABC, abstractmethod
from typing import List, Optional
import pendulum
from room import Room
from hotel import Hotel
from dataclasses import dataclass

@dataclass
class Booking:
    id: str
    room_id: str
    check_in: date
    check_out: date
    guest_count: int

    def __repr__(self):
        return f'Booking {self.room_id}, check in date - {self.check_in}, check out date {self.check_out}'
    
class BookingRepository(ABC):

    @abstractmethod
    def create_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        pass

    @abstractmethod
    def get_booking_by_room(self, room_id: str) -> List[Booking]:
        pass

    @abstractmethod
    def update_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def delete_booking(self, booking_id: str) -> None:
        pass

# Implementing storage in memory (Реализация хранилища в памяти)
class InMemoryRepository(BookingRepository):
    
    def __init__(self):
        self.bookings: List[Booking] = []

    def create_booking(self, booking: Booking) -> None:
        self.bookings.append(booking)

    def  get_booking(self, booking_id):
        for booking in self.bookings:
            if booking.id == booking_id:
                return booking
        return None
            
    def get_booking_by_room(self, booking_id) -> List[Booking]:
        return [booking for booking in self.bookings if booking_id == booking.id]
    
    def update_booking(self, booking: Booking) -> None:
        for index, existing_booking in enumerate(self.bookings):
            if existing_booking.id == booking.id:
                self.bookings[index] = booking
                return
        raise ValueError(f'Booking ID {booking.id} not found')
    
    def delete_booking(self, booking_id: int) -> None:
        self.bookings = [booking for booking in self.bookings if booking_id == booking.id]
    
class BookingManager:
    def __init__(self, repository: BookingRepository, hotels: List[Hotel]):
        self.repository = repository
        self.hotel = {hotel.id: hotel.name for hotel in hotels} #????

    def is_available(
            self, 
            room_id: str, 
            check_in: date, 
            check_out: date, 
            exclude_booking_id: str
            ) -> None:
        
        if check_out <= check_in:
            raise ValueError
        
        bookings = self.repository.get_booking_by_room(room_id)
        for booking in bookings:
            if exclude_booking_id and booking.id == exclude_booking_id:
                continue
            if not (check_out <= booking.check_in or check_in >= booking.check_out):
                return False
        return True
        

        

        
    
        

            