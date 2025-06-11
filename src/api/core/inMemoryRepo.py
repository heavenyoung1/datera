from src.api.core.bookingRepo import BookingRepository
from typing import List, Optional
from src.api.core.booking import Booking
import pendulum
from typing import Dict

class InMemoryRepository(BookingRepository):
    """ Реализация BookingRepository для хранения бронирований в памяти.

        Используется для прототипирования и тестирования.

        :ivar bookings: Список хранимых бронирований.
        :vartype bookings: List[Booking]
    """

    def __init__(self):
        self.bookings: Dict[str, Booking] = {}

    def create_book(self, booking: Booking) -> None:
        self.bookings[booking.id] = booking

    def get_booked_by_id(self, booking_id: str) -> Optional[Booking]:
        return self.bookings.get(booking_id)
    
    def get_booked_room(self, room_id: str, date: pendulum.DateTime) -> Optional[Booking]:
        for booking in self.bookings.values():
            if (room_id == booking.room_id):
                 return booking
        return None

    def update_book(self, booking_id: str, check_in: pendulum.DateTime, check_out: pendulum.DateTime) -> Booking:
        booking = self.get_booked_by_id(booking_id)
        if not booking:
            raise ValueError(f'Booking {booking_id} not found')
        
        booking.check_in = check_in
        booking.check_out = check_out
        return booking

    def delete_book(self, booking_id: str) -> None:
        if booking_id not in self.bookings:
            return None
        return self.bookings[booking_id]
