from random import randint

#includes cabinets, chests, dressers, drawers, closets, bags, satchels
class Box:
    #names (all recognizable names of box), items (lists); locked (bool); capacity (int)
    def __init__(self, names, items, locked=True, capacity=4, material="wood"):
        self.names = names
        self.items = items
        self.locked = locked
        self.capacity = capacity
        self.material = material
    #consider making this the open command
    def list_items(self):
        num = randint(1, 3)
        if num == 1:
            if len(self.items) == 1:
                print("Inside is", end=" ")
            else:
                print("Inside are", end =" ")
        elif num == 2:
            print("Inside you find", end=" ")
        elif num == 3:
            if len(self.items) == 1:
                print("Inside the", self.names[0], "is", end=" ")
            else:
                print("Inside the", self.names[0], "is", end=" ")
        for i in range(len(self.items)):
            if i+1 == len(self.items):
                if len(self.items) == 1:
                    print((self.items[i]).description, end=".\n")
                else:
                    print("and", (self.items[i]).description, end=".\n")
            else:
                print((self.items[i]).description, end=", ")


#includes tables, counters
class Table:
    def __init__(self, names, items, material="wood"):
        self.names = names
        self.items = items
        self.material = material
    def list_items():
        pass
        


#with and without drawers (initialize drawers with Boxes)
#(name drawers top and bottom)
class Desk:
    def __init__(self, names, items, drawers, material="wood"):
        self.names = names
        self.items = items
        self.drawers = drawers
        self.material = material

