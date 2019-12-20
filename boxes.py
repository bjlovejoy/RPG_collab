#includes cabinets, chests, 
class Box:
    def __init__(self, name, locked, capacity):
        self.name = name
        self.locked = locked
        self.capacity = capacity
    #consider making this the open command
    def description():
        print("Inside is ", end="")
        
#includes tables, counters, desktops
class Table:
    def __init__(self, locked, material, description):
        self.locked = locked
        self.material = material
        self. description = description
        
#includes dressers, desks with drawers
class Drawer:
    def __init__(self, locked, material, description):
        self.locked = locked
        self.material = material
        self. description = description

class Closet:
    def __init__(self, locked, material, description):
        self.locked = locked
        self.material = material
        self. description = description

