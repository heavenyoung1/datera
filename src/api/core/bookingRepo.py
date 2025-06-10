from dataclasses import dataclass
from abc import ABC, abstractmethod
from src.api.core.booking import Booking
from typing import Optional, List
from pendulum import date

@dataclass
class BookingRepository(ABC):
    """ Абстрактный интерфейс для работы с хранилищем бронирований.

        Определяет методы для создания, получения и удаления бронирований.
        Конкретные реализации должны предоставить логику хранения данных.
    """
    @abstractmethod
    def create_book(self, booking: Booking) -> None:
        """ Сохраняет новое бронирование.

            :param booking: Объект бронирования.
            :type booking: Booking
        """
        pass

    @abstractmethod
    def read_book_by_id(self, booking_id: str) ->  Optional[Booking]:
        """Возвращает бронирование по идентификатору.

            :param booking_id: Уникальный идентификатор бронирования.
            :type booking_id: str
            :return: Объект бронирования или None, если не найдено.
            :rtype: Optional[Booking]
        """
        pass

    @abstractmethod
    def read_booked_room(self, room_id: str, date: date) -> Optional[Booking]:
        """ Возвращает бронирование для номера.

            :param room_id: Уникальный идентификатор номера.
            :type room_id: str
            :return: Объект бронирование для указанного номера.
            :rtype: Optional[Booking]
        """
        pass

    @abstractmethod
    def update_book(self, booking_id: str) -> Booking:
        """ Возвращает обновленный объект бронирования

            :param booking_id: Уникальный идентификатор бронирования.
            :type booking_id: str

            :return: Объект бронирования или None, если не найдено.
            :rtype: Booking
        """
        pass

    @abstractmethod
    def delete_book(self, booking_id: str) -> None:
        """ Удаляет бронирование по идентификатору.

            :param booking_id: Уникальный идентификатор бронирования.
            :type booking_id: str
            :raises ValueError: Если бронирование не найдено.
        """
        pass