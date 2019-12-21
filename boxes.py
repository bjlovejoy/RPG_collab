from random import randint
from colorama import Fore, Style

#************************************************************************

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
        if len(self.items) == 0:
            #add some more variations
            print("There's nothing inside.")
        else:
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
                    print("Inside the", self.names[0], "are", end=" ")
            for i in range(len(self.items)):
                if i+1 == len(self.items):
                    if len(self.items) == 1:
                        print((self.items[i]).description, end=".\n")
                    else:
                        print("and", (self.items[i]).description, end=".\n")
                else:
                    print((self.items[i]).description, end=", ")


    #item is a list of strings, can do multiple
    #need to handle empty boxes and if command called when not at box
    def remove_item(self, item):
        copy_item = []
        for i in item:
            exist = False
            itr = 0
            for j in self.items:
                for k in j.names:
                    if i == k:
                        exist = True
                        num = itr
                itr += 1
            if exist:
                copy_item.append(self.items[num])
                del self.items[num]  #also need to pass item to player inventory
        if len(copy_item) > 0:
            return copy_item
        else:
            return None  #in main, if not None, give to player
    
    #print one item at a time as it is removed
    def remove_all(self):
        copy_item = []
        for i in range(len(self.items)):
            copy_item.append(self.items[0])
            del self.items[0]
        if len(copy_item) > 0:
            return copy_item
        else:
            return None  #in main, if not None, give to player
    
    #item is a list, can do multiple
    #print one item at a time as added
    def add_item(self, item):
        (self.items).append(item)


#************************************************************************


#includes tables, counters
class Table:
    def __init__(self, names, items, material="wood"):
        self.names = names
        self.items = items
        self.material = material
    def list_items(self):
        num = randint(1, 3)
        if num == 1:
            if len(self.items) == 1:
                print("On top is", end=" ")
            else:
                print("On top are", end =" ")
        elif num == 2:
            print("On top you find", end=" ")
        elif num == 3:
            if len(self.items) == 1:
                print("On the", self.names[0], "is", end=" ")
            else:
                print("On the", self.names[0], "is", end=" ")
        for i in range(len(self.items)):
            if i+1 == len(self.items):
                if len(self.items) == 1:
                    print((self.items[i]).description, end=".\n")
                else:
                    print("and", (self.items[i]).description, end=".\n")
            else:
                print((self.items[i]).description, end=", ")


#************************************************************************


#must include drawers
#(initialize desktop with a table and drawers with Boxes)
#(name drawers top and bottom)
class Desk:
    def __init__(self, names, desktop, drawers, material="wood"):
        self.names = names
        self.desktop = desktop
        self.drawers = drawers
        self.material = material

