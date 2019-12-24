from colorama import Fore, Style


#make sure description starts with lowercase letter unless intended capital
class Item:
    def __init__(self, names, description):
        self.names = names
        self.description = description
    def look(self):
        print((self.description.capitalize()))
        

class Weapon:
    def __init__(self, names, style, description):
        self.names = names
        self.style = style
        self.description = description
    def look(self):
        print((self.description.capitalize()))


#make interactable item, such as guess riddle answer

#make key class or key subclass (consider part of Door)
