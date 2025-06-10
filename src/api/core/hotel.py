from dataclasses import dataclass
from typing import List

from src.api.core.room import Room

@dataclass
class Hotel:
    """ Модель отеля, содержащая информацию о нём и его номерах.

        :ivar id: Уникальный идентификатор отеля.
        :vartype id: str
        :ivar name: Название отеля.
        :vartype name: str
        :ivar city: Город, где расположен отель.
        :vartype city: str
        :ivar address: Адрес отеля.
        :vartype address: str
        :ivar metro_stations: Список ближайших станций метро.
        :vartype metro_stations: List[str]
        :ivar rooms: Список номеров в отеле.
        :vartype rooms: List[Room]
        
    """
    id: str
    name: str
    city: str
    address: str
    metro_stations: List[str]
    rooms: List[Room]

    def __repr__(self):
        return f'Hotel with ID {self.id}, {self.id}, name - {self.name}, rooms {self.rooms}'