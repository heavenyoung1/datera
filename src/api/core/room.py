class Room:
    def __init__(
            self,
            id: int,
            name: str,
            capacity: int,
            price: int,
            hotel_id: int
                ):
        self.id = id
        self.name = name 
        self.capacity = capacity
        self.price = price
        self.hotel_id = hotel_id

    def __repr__(self):
        return f'Booking {self.name}, capacity - {self.capacity}, price per night {self.price}'
    
    def __eq__(self, value):
        pass #Реализовать функцию сравнения
