from dataclasses import dataclass
from pendulum import DateTime

@dataclass
class Booking:
    """ Модель бронирования номера.

        :ivar id: Уникальный идентификатор бронирования.
        :vartype id: str
        :ivar hotel_id: ID отеля.
        :vartype hotel_id: str
        :ivar room_id: ID номера.
        :vartype room_id: str
        :ivar guest_count: Количество гостей.
        :vartype guest_count: int
        :ivar check_in: Дата заезда.
        :vartype check_in: date
        :ivar check_out: Дата выезда.
        :vartype check_out: date
    """

    id: str
    hotel_id: str
    room_id: str
    guest_count: int
    check_in: DateTime
    check_out: DateTime