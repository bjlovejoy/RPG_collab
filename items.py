
#make sure description starts with lowercase letter unless intended capital
class Item:
    def __init__(self, names, description):
        self.names = names
        self.description = description
    def look(self):
        print((self.description.capitalize()))
        

class Weapon:
    def __init__(self, name, style, description):
        self.name = name
        self.style = style
        self.description = description
    def look(self):
        print((self.description.capitalize()))


#make interactable item, such as guess riddle answer
