from colorama import Fore, Style


class Command:
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords

quit = Command("quit", ["quit", "exit", "end", "q"])

look = Command("look", ["look", "see", "study", "view", "check"])
go = Command("go", ["go", "walk", "run", "travel", "head", "leave"])
opens = Command("open", ["open", "enter", "unlock"])
close = Command("close", ["close"])

take = Command("take", ["take", "grab"])
put = Command("put", ["put", "place"])

use = Command("use", ["use", "interact", "try"])  #need to equip before using if equipable
equip = Command("equip", ["equip"])

eat = Command("eat", ["eat", "drink"])
touch = Command("touch", ["touch", "feel"])

#attack, fight, build, create, talk to, push, set, lay, place, drop, remove
#feel, cast, light, poop/pee, curse words, yell, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into)

allCmds = [quit, look, go, opens, close, take, put, use, equip, eat]



def parseCmd(cmd, room, player, loc):
    said = "None"
    for i in allCmds:
        for j in (i.keywords):
            if cmd[0] == j:
                said = i.name  #consider command confusion (multiple potential options)
    
    if said == "look":
        LOOK(cmd, room, player)
    elif said == "go":
        GO()
    elif said == "quit":
        #function to prompt saving to text doc (call separate save function)
        QUIT()
        return False
    else:
        print(Fore.RED + "I don't know what you're saying.")
        print(Style.RESET_ALL, end="", flush=True)
    return True



def QUIT():
    pass
    


#for looking in chests or at specific objects in chest,
#consider positional attribute in room class for which
#quadrant the player is in (does not always have to apply
#(default to None)
def LOOK(cmd, room, player):
    atCmd = False
    
    if len(cmd) == 1:
        room.look()
        
    elif (cmd[1] == "around" or cmd[1] == "room" or cmd[1] == "here") and len(cmd) == 2:
        room.look()
        
    elif (cmd[1] == "at" or cmd[1] == "for") and len(cmd) > 2:
        for i in range(2):
            del cmd[0]
        atCmd = True
    
    else:
        del cmd[0]          #includes view, study, see, etc.
        atCmd = True        #also cases like "look key"
    
    if atCmd:
        a = " "
        item = a.join(cmd)
        
        center = -1
        inventory = -2
        
        if player.roomLoc == center:  #need to find what user is talking about
            count = 0                 #(chest, door, item, NPC), does not include inside chests
            description = ""
            for i in room.quads:
                if i != None:
                    for j in i.names:
                        if j == item:
                            count += 1
                            description = i.description
            if count > 1:
                print("There are multiple.  Plese refine.")  #duplicates
                                                             #TODO add more and color
            
            elif count == 0:
                print("I could not find any.")  #TODO add more and color
            
            else:
                print(description)
        
        elif player.roomLoc == inventory:  #search through inventory
            count = 0                      #(includes equipped gear)
            description = ""
            for i in (player.inventory).items:
                for j in i.names:
                    if j == item:
                        count += 1
                        description = i.description
            if count > 1:
                print("There are multiple.  Plese refine.")  #duplicates
                                                             #TODO add more and color
            
            elif count == 0:
                print("I could not find any.")  #TODO add more and color
            
            else:
                print(description)
        
        else:       #lies in quds 0-7, look in chests, interact with items
                    #find out object type and use .names attribute
                    #If interacting with item, need to search items on item
            if quads[(player.roomLoc)] == Box:
                for i in quads[(player.roomLoc)].items:
                    for j in i.names:
                        if j == item:
                            count += 1
                            description = i.description
                if count > 1:
                    print("There are multiple.  Plese refine.")  #duplicates
                                                                #TODO add more and color
                
                elif count == 0:
                    print("I could not find any.")  #TODO add more and color
                
                else:
                    print(description)
            
            if quads[(player.roomLoc)] == item:
                pass
            
            elif quads[(player.roomLoc)] == NPC:
                if:
                    pass    #check if looking at NPC
                else:
                    pass    #checkif looking at NPCs items/inventory


#may need to add look statement for chests

"""
need to "open" and "close" chests, inventory

look at:    door
            chest
            inventory
            room
            item in room
            item in chest
            item in inventory
            NPCs
            weapon
            equipped items/armor/weapons
"""





def GO(cmd, room, player, allRooms):
    direction = cmd[1][0]  #sends first character of direction
    
    if len(cmd) < 2:
            #consider turning this into a function (pass text and color)
            print(Fore.RED + "Specify direction")
            print(Style.RESET_ALL, end="", flush=True)
            
    elif direction == "n" or direction == "s" or direction == "e" or direction == "w":
        location(direction, loc, allRooms)
    
    else:
        print(Fore.RED + "I'm not sure where that's at.")  #TODO add more
        print(Style.RESET_ALL, end="", flush=True)





















