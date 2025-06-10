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
        pass 
    # Здесь нужно реаолизовать поиск бронирования по дате и номеру
    # И вернуть нужное бронирование, если дата в пределах бронирования и номер комнаты существует
             

    def update_book(self, booking_id: str, check_in: Date, check_out: Date) -> Booking:
        pass 
        # Здесь нужно по надйенному бронированию обновить его, 
        # И в зависимости от того, какие данные обновить их
        searches_books = self.get_booked_room()

    def delete_book(self, booking_id):
        pass
