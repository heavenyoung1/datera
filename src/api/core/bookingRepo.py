from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class BookingRepository(ABC):
    """ Интерфейс для работы с хранилищем """
    @abstractmethod
    def create_book(self):
        pass

    @abstractmethod
    def read_book(self):
        pass

    @abstractmethod
    def update_book(self):
        pass

    @abstractmethod
    def delete_book(self):
        pass