from datetime import date
from abc import ABC, abstractmethod
from typing import List, Optional
import pendulum
from room import Room
from hotel import Hotel
from dataclasses import dataclass

@dataclass
class Booking:
    id: str
    room_id: str
    check_in: date
    check_out: date
    guest_count: int

    def __repr__(self):
        return f'Booking {self.room_id}, check in date - {self.check_in}, check out date {self.check_out}'
    
class BookingRepository(ABC):

    @abstractmethod
    def create_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def get_booking(self, booking_id: str) -> Optional[Booking]:
        pass

    @abstractmethod
    def get_booking_by_room(self, room_id: str) -> List[Booking]:
        pass

    @abstractmethod
    def update_booking(self, booking: Booking) -> None:
        pass

    @abstractmethod
    def delete_booking(self, booking_id: str) -> None:
        pass

# Implementing storage in memory (Реализация хранилища в памяти)
class InMemoryRepository(BookingRepository):
    
    def __init__(self):
        self.bookings: List[Booking] = []

    def create_booking(self, booking: Booking) -> None:
        self.bookings.append(booking)

    def  get_booking(self, booking_id):
        for booking in self.bookings:
            if booking.id == booking_id:
                return booking
        return None
            
    def get_booking_by_room(self, booking_id) -> List[Booking]:
        return [booking for booking in self.bookings if booking_id == booking.id]
    
    def update_booking(self, booking: Booking) -> None:
        for index, existing_booking in enumerate(self.bookings):
            if existing_booking.id == booking.id:
                self.bookings[index] = booking
                return
        raise ValueError(f'Booking ID {booking.id} not found')
    
    def delete_booking(self, booking_id: int) -> None:
        self.bookings = [booking for booking in self.bookings if booking_id == booking.id]
    
class BookingManager:
    """ Менеджер бронирований для управления процессом бронирования номеров в отелях.

    Этот класс отвечает за бизнес-логику, связанную с созданием, обновлением, удалением
    бронирований, а также проверкой доступности номеров и дат.

    Args:
        repository (BookingRepository): Репозиторий для хранения данных о бронированиях.
        hotels (List[Hotel]): Список отелей, содержащих информацию о номерах.
    """
    
    def __init__(self, repository: BookingRepository, hotels: List[Hotel]):
        self.repository = repository
        self.hotel = {hotel.id: hotel.name for hotel in hotels} #????

    def is_available(
            self, 
            room_id: str, 
            check_in: date, 
            check_out: date, 
            exclude_booking_id: str
            ) -> None:
        
        """Проверяет доступность номера на заданные даты.

        Метод проверяет, свободен ли номер с указанным ID в заданный период, учитывая
        существующие бронирования. Если указано `exclude_booking_id`, соответствующее
        бронирование игнорируется (используется при обновлении дат бронирования).

        Args:
            room_id (str): Уникальный идентификатор номера.
            check_in (date): Дата заезда.
            check_out (date): Дата выезда.
            exclude_booking_id (Optional[str], optional): ID бронирования, которое
                следует исключить из проверки (например, при обновлении). Defaults to None.

        Returns:
            bool: True, если номер доступен, False в противном случае.

        Raises:
            None: Метод не выбрасывает исключений, но возвращает False при некорректных датах
                (check_out <= check_in).
        """
        
        if check_out <= check_in:
            raise ValueError
        
        bookings = self.repository.get_booking_by_room(room_id)
        for booking in bookings:
            if exclude_booking_id and booking.id == exclude_booking_id:
                continue
            if not (check_out <= booking.check_in or check_in >= booking.check_out):
                return False
        return True

    def _get_room():
        

        

        
    
        

            