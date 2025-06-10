import pytest
from pendulum import date
from src.api.core.booking import Booking, InMemoryRepository 

class TestInMemoryRepository:

    @pytest.fixture()
    def repository(self):
        return InMemoryRepository()
    
    @pytest.fixture
    def sample_booking(self):
        """Фикстура для создания тестового бронирования"""
        return Booking(
            id="b1",
            room_id="r1", 
            check_in=date(2024, 12, 1),
            check_out=date(2024, 12, 5),
            guest_count=2
        )
    
    def test_create_booking(self, repository, sample_booking):
        repository.create_booking(sample_booking)
        assert len(repository.bookings) == 1
        assert repository.bookings[0].id == "b1"
