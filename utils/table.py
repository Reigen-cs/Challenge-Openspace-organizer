class Seat:
    def __init__(self):
        self.free = True
        self.occupant = ""
    
    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

class Table:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def has_free_spot(self):
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False