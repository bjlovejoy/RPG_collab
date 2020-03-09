from colorama import Fore, Style


#make sure description starts with lowercase letter unless intended capital

#short description for Box list, long for Look (set long to None, if None, set to short)
class Item:
    def __init__(self, names, description, equipable=False):
        self.names = names
        self.description = description
        self.equipable = equipable
        self.equiped = False
    def look(self):
        print((self.description.capitalize()))
    def equip:
        pass
    def unequip:
        pass
        

class Weapon:
    def __init__(self, names, style, description):
        self.names = names
        self.style = style
        self.description = description
    def look(self):
        print((self.description.capitalize()))

class Interactable(self, names, description):   #if cmd is done, engage event
    def __init__(self, names, description):
        self.names = names
        self.description = description

#give promt, wait for response
#if correct, change room/player state or give items/text to proceed


#make interactable item, such as guess riddle answer (make need to incorporate Box())

#make key class or key subclass (consider part of Door)
