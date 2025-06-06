
class Seat:
    def __init__(self, free=True, occupant=""):
        self.free = free
        self.occupant =occupant

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free =False
            return f"Seat assigned to {self.occupant}"
        return "Seat was occupied"
    
    def remove_occupant(self):
        if not self.free:
            previous_occupant = self.occupant
            self.occupant = ""
            self = True
            return f"{previous_occupant}, was removed from table"
        return "Seat was free"
    




    class Table:
        def __init__(capacity=0, seats=[])


    

    
