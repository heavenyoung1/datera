from dataclasses import dataclass
from src.api.core.bookingRepo import BookingRepository

@dataclass
class InMemoryRepository(BookingRepository):
    """ Интерфейс для работы с хранилищем """
    pass