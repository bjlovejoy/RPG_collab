from colorama import Fore, Style


def createPlayer():
    #Add prompts
    player = Player("Brendon")
    return player





#see notebook for additional player attributes
class Player:
    inventory = Box()
    roomLoc = 
    
    def __init__(self, name):
        self.name = name
    def addToInv(self, items):
        inventory.add_item(items)
    def remFromInv(self, items):
        copy_items = inventory.remove_item(items)
        return copy_items
    def clearInv(self):
        inventory.remove_all()




class NPC:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory



#consider location as player method
def location(direction, loc, allRooms):
    able = True
    
    if direction == "n" and loc > 9:
        if allRooms[loc] != None:
            loc -= 10
        else:
            able = False
            
    elif direction == "s" and loc < 90:
        if allRooms[loc] != None:
            loc += 10
        else:
            able = False
            
    elif direction == "e" and loc % 10 != 9:
        if allRooms[loc] != None:
            loc += 1
        else:
            able = False
            
    elif direction == "w" and loc % 10 != 0:
        if allRooms[loc] != None:
            loc -= 1
        else:
            able = False
    
    if able == False:
        print("You can't go that way")  #TODO add more text
