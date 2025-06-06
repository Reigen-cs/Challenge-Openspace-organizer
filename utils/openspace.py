import random
from table import Table

class Openspace:
    def __init__(self, number_of_tables=6):
        self.tables = [Table() for _ in range(number_of_tables)]
    
    def organize(self, names):
        random.shuffle(names)
        
        for name in names:
            assigned = False
            
            # Try to assign to existing tables
            for table in self.tables:
                if table.has_free_spot():
                    if table.assign_seat(name):
                        assigned = True
                        break
            
            # If no space, add a new table
            if not assigned:
                new_table = Table()
                new_table.assign_seat(name)
                self.tables.append(new_table)
                print(f"Added new table for {name}")
    
    def display(self):
        print("\nOpenspace Layout:")
        for i, table in enumerate(self.tables):
            print(f"\nTable {i+1}:")
            for j, seat in enumerate(table.seats):
                if seat.free:
                    print(f"  Seat {j+1}: Empty")
                else:
                    print(f"  Seat {j+1}: {seat.occupant}")