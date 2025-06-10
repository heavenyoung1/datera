from dataclasses import dataclass

@dataclass
class Room:
    """ Модель номера в отеле.

        :ivar id: Уникальный идентификатор номера.
        :vartype id: str
        :ivar type: Тип номера (например, "Люкс", "Стандарт").
        :vartype type: str
        :ivar max_guests: Максимальное количество гостей.
        :vartype max_guests: int
        :ivar floor: Этаж, на котором расположен номер.
        :vartype floor: int
        :ivar price: Цена за ночь.
        :vartype price: int
        :ivar hotel_id: ID отеля, к которому относится номер.
        :vartype hotel_id: str
    """

    id: str
    type: tuple
    max_guests: int
    floor: int
    price: int
    hotel_id: str