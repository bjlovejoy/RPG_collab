from colorama import Fore, Style


def createPlayer():
    #Add prompts
    player = Player("Brendon")
    return player


#make the player also hold the main loc
#make player have in-between rooms bool (or LAST_LOC var)


#see notebook for additional player attributes
class Player:
    self.inventory = Inventory()
    self.room_loc = -1  #Here, -1 (center tile), -2 (inventory) and 0-7 are quads
    self.map_loc = 0    #location of player in level
    
    def __init__(self, name):
        self.name = name
        
    def enter_inventory(self):
        self.room_loc = -2
        
    def show_stats(self):
        pass


#treat like box, but with custom features (slots hold item, if equipped)
class Inventory():
    def __init__(self):
        pass

    def list_contents(self):
        pass
    
    def list_filter(self, filter):  #can pass multiple filters
        pass                        #(potions, food, rations, weapons, equipped, unequipped)
    
    def add_item(self, item):
        pass
    
    def remove_item(self, item):
        pass
    
    def equip_item(self, item):
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


