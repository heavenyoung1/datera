import pendulum
from src.api.core.hotel import Hotel
from src.api.core.room import Room
from src.api.core.inMemoryRepo import InMemoryRepository
from src.api.core.bookingManager import BookingManager

# Создаем тестовые данные
class MockRepository(InMemoryRepository):
    def get_booked_room(self, room_id: str, date: pendulum.DateTime) -> bool:
        return False  # Все номера свободны для теста
    
    def create_book(self, booking):
        print(f"Бронирование создано в репозитории: {booking.id}")

# Создаем тестовый отель с номером
test_hotel = Hotel(id="hotelw_1", name="Test Hotel", city="Moscow", address="Golubkin Street", metro_stations=['Lenina'], rooms=3)
test_room = Room(id="room_101", type=("VIP") , max_guests=3, floor=44, price=2500 , hotel_id="hotel_1")
test_hotel.rooms = [test_room]

# Создаем BookingManageri
manager = BookingManager(
    repository=MockRepository(),
    hotels=[test_hotel]
)

# Тестовые параметры бронирования
test_check_in = pendulum.datetime(2025, 6, 10)#.date()
test_check_out = pendulum.datetime(2025, 6, 15)#.date()
print(test_check_in)

# Вызываем метод book
try:
    booking = manager.book(
        room_id=test_room.id,
        guest_count=2,
        check_in=test_check_in,
        check_out=test_check_out
    )
    print(f"Бронирование успешно создано: {booking.id}")
except ValueError as e:
    print(f"Ошибка бронирования: {e}")