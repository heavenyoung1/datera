from src.api.core.hotel import Hotel
from src.api.core.room import Room
from src.api.core.booking import Booking 

from pendulum import date

class TestModel:
    """ Тест для моделей данных (dataclasses) """

    def test_hotel_creation(self):
        hotel = Hotel(id='00101', name='Test Hotel', rooms=90)
        assert hotel.id == '1'
        assert hotel.name == 'Test Hotel'
        assert hotel.rooms == 90

    def test_room_creation(self):
        room = Room(id='00101090', name='Luxury', capacity=3, price=2500, hotel_id='00101')
        assert room.id == "00101090"
        assert room.capacity == 3
        assert room.hotel_id == "00101"

    def test_booking_creation(self):
        booking =  Booking(
            id='110101010110101',
            room_id='00101090',
            check_in=date(2025, 12, 1),
            check_out=date(2025, 12, 12),
            guest_count=3
        )
        assert booking.id == '110101010110101'
        assert booking.room_id == '00101090'
        assert booking.guest_count == 3