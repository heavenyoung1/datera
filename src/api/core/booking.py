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
        self.hotels = {hotel.id: hotel for hotel in hotels} #????

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

    def _get_room(self, room_id: str) -> Optional[Room]:
        """Вспомогательный метод для поиска номера по ID.

        Метод проходит по всем отелям и их номерам, возвращая объект Room с указанным ID,
        если он существует.

        Args:
            room_id (str): Уникальный идентификатор номера.

        Returns:
            Optional[Room]: Объект Room, если номер найден, иначе None.

        Raises:
            None: Метод не выбрасывает исключений, возвращает None при отсутствии номера.

        Note:
            Этот метод предназначен для внутреннего использования в классе BookingManager.
        """
        for hotel in self.hotels.values():
            for room in hotel.rooms:
                if room.id == room_id:
                    return room
            return None

    def book(self, room_id: str, check_in: date, check_out: date, guest_count: int) -> Booking:
        """Создаёт новое бронирование для номера.

        Метод создаёт бронирование, проверяя доступность номера, корректность дат и
        соответствие количества гостей вместимости номера. После успешной проверки
        бронирование сохраняется в репозитории.

        Args:
            room_id (str): Уникальный идентификатор номера.
            check_in (str): Дата заезда в формате, поддерживаемом pendulum (например, "YYYY-MM-DD").
            check_out (str): Дата выезда в формате, поддерживаемом pendulum (например, "YYYY-MM-DD").
            guest_count (int): Количество гостей.

        Returns:
            Booking: Объект созданного бронирования с уникальным ID.

        Raises:
            ValueError: Если дата выезда раньше или равна дате заезда, номер не существует,
                количество гостей превышает вместимость номера, или номер недоступен на
                указанные даты.
        """
        check_in_date = pendulum.parse(check_in).date()
        check_out_date = pendulum.parse(check_out).date()

        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")
        
        # Проверяем, существует ли номер
        room = self._get_room(room_id)
        if not room:
            raise ValueError(f"Room ID {room_id} not found")
        
        # Проверяем вместимость
        if guest_count > room.capacity:
            raise ValueError(f"Guest count {guest_count} exceeds room capacity {room.capacity}")

        if not self.is_available(room_id, check_in_date, check_out_date):
            raise ValueError("Room is not available for the selected dates")
        
        booking = Booking(

        )



repo = InMemoryRepository()

# Допустим, у нас есть номер "room1"Add commentMore actions
room = Room('id1' ,'name1', 4, 2500, 'hotel_idb1')
room = Room('id1' ,'name1', 4, 2500, 'hotel_idb1')
hotel = Hotel("hotel1", "Test Hotel", [room])
manager = BookingManager(repo, [hotel])

# Добавим бронирование с 10 по 15 июня
existing_booking = Booking(id="b1", room_id="room1", check_in=date(2025, 6, 10), check_out=date(2025, 6, 15), guest_count=1)
repo.create_booking(existing_booking)

# # Тест 1: проверим пересечение (например, с 12 по 17 июня) → False
# print(manager.is_available("room1", date(2025, 6, 12), date(2025, 6, 17), 1))  # ❌ False

# # Тест 2: проверим свободный диапазон (например, с 5 по 9 июня) → True
# print(manager.is_available("room1", date(2025, 6, 5), date(2025, 6, 9)))  # ✅ True

# # Тест 3: заезд в день выезда (15 июня) → True
# print(manager.is_available("room1", date(2025, 6, 15), date(2025, 6, 18)))  # ✅ True

# # Тест 4: заезд = выезд (некорректно) → False
# print(manager.is_available("room1", date(2025, 6, 20), date(2025, 6, 20)))  # ❌ False

print(manager.hotels)

       

        

        
    
        

            