from src.api.core.validator import Validator
from src.api.core.hotel import Hotel
from typing import List, Optional
from src.api.core.bookingRepo import BookingRepository
from pendulum import (Date, parse as pendulum_parser, duration)
from src.api.core.booking import Booking
from uuid import uuid4

class BookingManager:
    """Менеджер бронирований, реализующий бизнес-логику.

        Координирует работу с отелями, номерами, бронированиями и валидацией.

        :ivar repository: Хранилище бронирований.
        :vartype repository: BookingRepository
        :ivar hotels: Список отелей.
        :vartype hotels: List[Hotel]
        :ivar validator: Объект для валидации данных.
        :vartype validator: Validator
    """

    def __init__(self, repository: BookingRepository, hotels: List[Hotel]):
        self.repository = repository
        self.hotels = hotels
        self.validator = Validator()

    def _get_room(self, room_id: str):
        for hotel in self.hotels:
            for room in hotel.rooms:
                if room_id == room.id:
                    return room
        return None
    
    def _get_hotel(self, hotel_id: str) -> Optional[Hotel]:
        """Ищет отель по идентификатору.

        :param hotel_id: Уникальный идентификатор отеля.
        :type hotel_id: str
        :return: Объект отеля или None, если не найден.
        :rtype: Optional[Hotel]
        """
        for hotel in self.hotels:
            if hotel.id == hotel_id:
                return hotel
        return None

    def is_available(self, room_id: str, check_in: Date, check_out: Date) -> bool:
        """ Проверяет доступность номера на заданные даты """
        self.validator._validate_dates(check_in, check_out)
        current_date = check_in
        while current_date <= check_out:
            if self.repository.get_booked_room(room_id, current_date):
                return False
            current_date += duration(days=1)
        return True
    
    def book(self, room_id: str, guest_count: int, check_in: Date, check_out: Date):
        check_in_date = pendulum_parser(check_in) #Это какая-то шляпа, нужно придумать лучше!!
        check_out_date = pendulum_parser(check_out)
        room = self._get_room(room_id)

        self.validator.validate_booking(
            self,
            check_in=check_in_date,
            check_out=check_out_date,
            room=room,
            guest_count=guest_count,
        )

        if not self.is_available(room_id, check_in, check_out):
            raise ValueError("Room is not available for the selected dates")
        
        booking = Booking(
            id=str(uuid4),
            hotel_id=room.hotel_id,
            room_id=room_id,
            guest_count=guest_count,
            check_in=check_in_date,
            check_out=check_out_date,
        )

        self.repository.create_book(booking)
        return booking

        
