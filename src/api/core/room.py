class Room:
    def __init__(
            self,
            id: int,
            name: str,
            capacity: int,
            price: int,
                ):
        self.id = id
        self.name = name 
        self.capacity = capacity
        self.price = price

    def __repr__(self):
        return f'Booking {self.name}, capacity - {self.capacity}, price per night {self.price}'
    
    def __eq__(self, value):
        pass #Реализовать функцию сравнения
