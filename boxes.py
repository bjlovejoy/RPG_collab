#includes cabinets, chests, 
class Box:
    #names, items (lists); locked (bool); capacity (int)
    def __init__(self, names, items, locked, capacity):
        self.names = names
        self.items = items
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

