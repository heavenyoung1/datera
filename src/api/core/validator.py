from pendulum import Date
from typing import Optional
from src.api.core.room import Room
from src.api.core.hotel import Hotel

class Validator:
    """Класс для валидации данных бронирования.

        Проверяет корректность дат, количества гостей и существование сущностей.
    """

    def validate_dates(self, check_in: Date, check_out: Date) -> None:
        pass

    def validate_guests(self, room: Room, guest_count: int) -> None:
        pass

    def validate_room(self, room: Optional[Room]) -> None:
        pass

    def validate_hotel(self, hotel: Optional[Hotel]) -> None:
        pass
