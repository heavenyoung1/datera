from pendulum import Date
from typing import Optional
from src.api.core.room import Room
from src.api.core.hotel import Hotel

class Validator:
    """Класс для валидации данных бронирования.

        Проверяет корректность дат, количества гостей и существование сущностей.
    """

    def _validate_dates(self, check_in: Date, check_out: Date) -> None:
        """ Проверяет, что дата выезда позже даты заезда """
        if check_in <= check_out:
            raise ValueError("Check-out date must be after check-in date")

    def _validate_guests(self, room: Room, guest_count: int) -> None:
        """ Проверяет, что количество гостей не превышает вместимость номера """
        if guest_count > room.max_guests:
            raise ValueError(f"Guest count {guest_count} exceeds room capacity {room.max_guests}")

    def _validate_room(self, room: Optional[Room]) -> None:
        """ Проверяет, что номер существует """
        if not room:
            raise ValueError("Room not found")

    def _validate_hotel(self, hotel: Optional[Hotel]) -> None:
        """Проверяет, что отель существует """
        if not hotel:
            raise ValueError("Hotel not found")
        
    def validate_booking(
        self,
        check_in: Date,
        check_out: Date,
        room: Optional[Room],
        #hotel: Optional[Hotel],
        guest_count: int,
    ) -> None:
        """Комплексная валидация бронирования."""
        self._validate_room(room)
        self._validate_dates(check_in, check_out)
        self._validate_guests(room, guest_count)