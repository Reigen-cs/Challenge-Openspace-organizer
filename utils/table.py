class Seat:
    """
    Class representing a seat in the openspace.
    
    A seat can be free or occupied by a person.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new seat.
        
        By default, a seat is free and has no occupant.
        """
        self.free: bool = True
        self.occupant: str = ""
    
    def set_occupant(self, name: str) -> bool:
        """
        Assign someone to the seat if it's free.
        
        :param name: The name of the person to assign to the seat.
        :return: True if assignment was successful, False if seat was already occupied.
        """
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False


class Table:
    """
    Class representing a table in the openspace.
    
    A table has a certain capacity and contains multiple seats.
    """
    
    def __init__(self, capacity: int = 4) -> None:
        """
        Initialize a new table with the specified capacity.
        
        :param capacity: The number of seats at this table (default: 4).
        """
        self.capacity: int = capacity
        self.seats: list[Seat] = [Seat() for _ in range(capacity)]
    
    def has_free_spot(self) -> bool:
        """
        Check if the table has at least one free spot.
        
        :return: True if there's at least one free seat, False otherwise.
        """
        return any(seat.free for seat in self.seats)
    
    def assign_seat(self, name: str) -> bool:
        """
        Assign someone to the first available seat at the table.
        
        :param name: The name of the person to assign to a seat.
        :return: True if assignment was successful, False if no free seats.
        """
        for seat in self.seats:
            if seat.set_occupant(name):
                return True
        return False