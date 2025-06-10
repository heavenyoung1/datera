from dataclasses import dataclass
from src.api.core.bookingRepo import BookingRepository
from typing import List, Optional
from src.api.core.booking import Booking
from pendulum import Date


class InMemoryRepository(BookingRepository):
    """ Реализация BookingRepository для хранения бронирований в памяти.

        Используется для прототипирования и тестирования.

        :ivar bookings: Список хранимых бронирований.
        :vartype bookings: List[Booking]
    """

    def __init__(self):
        self.bookings: List[Booking] = []

    def create_book(self, booking) -> None:
        self.bookings.append(booking)

    def get_booked_by_id(self, booking_id: str) -> Optional[Booking]:
        for booking in self.bookings:
            if booking_id == booking.id:
                return booking
        return None
    
    def get_booked_room(self, room_id: str, date: Date):
        for booking in self.bookings:
            if (room_id == booking.room_id) and (date >= booking.check_in and date <= booking.check_out):
                return booking
        return None

    def update_book(self, booking_id: str, check_in: Date, check_out: Date) -> Booking:
        booking = self.get_booked_by_id(booking_id)
        if not booking:
            raise ValueError(f'Booking {booking_id} not found')
        
        booking.check_in = check_in
        booking.check_out = check_out
        return booking

    def delete_book(self, booking_id):
        pass
