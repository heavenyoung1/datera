from datetime import date

class Booking:
    def __init__(
            self,
            id: str,
            room_id: str,
            check_in: date,
            check_out: date,
    ):
        self.id = id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out