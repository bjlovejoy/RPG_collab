from colorama import Fore, Style


def createPlayer():
    #Add prompts
    player = Player("Brendon")
    return player


#make the player also hold the main loc
#make player have in-between rooms bool


#see notebook for additional player attributes
class Player:
    self.inventory = Box()
    self.roomLoc = -1  #Here, -1 (center tile), -2 (inventory) and 0-7 are quads
    self.mapLoc = 0    #location of player in level

    self.inBetween = False  #if player is between looking at a table and the center of the room
                            #if divert from table. automatically "leave" table
    
    def __init__(self, name):
        self.name = name
        
    def addToInv(self, items):
        inventory.add_item(items)
    
    def remFromInv(self, items):
        copy_items = inventory.remove_item(items)
        return copy_items
    
    def clearInv(self):
        inventory.remove_all()
    
    def equip:
        pass
    def unequip:
        pass




class NPC:
    self.inventoryOpen = False  #Is the player looking in their inventory (shopkeep)
    
    def __init__(self, names, description, inventory):
        self.names = names
        self.description = description
        self.inventory = inventory  #treat as Box



#consider location as player method
def location(direction, loc, allRooms):
    able = True
    
    if direction == "n" and loc % 100 > 9:
        if allRooms[loc] != None:
            loc -= 10
        else:
            able = False
            
    elif direction == "s" and loc % 100 < 90:
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
    
    #TODO: for traveling up and down (not implemented yet)
    """
    elif direction == "u" and loc < 900:
        if allRooms[loc] != None:
            loc += 100
        else:
            able = False
    
    elif direction == "d" and loc > 100:
        if allRooms[loc] != None:
            loc -= 100
        else:
            able = False
    """
    
    if able == False:
        print(Fore.RED + "You can't go that way")  #TODO add more text
        print(Style.RESET_ALL, end="", flush=True)


