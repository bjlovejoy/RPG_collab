from colorama import Fore, Style





def parseCmd(cmd, room, player, loc):
    said = "None"
    for i in allCmds:
        for j in (i.keywords):
            if cmd[0] == j:
                said = i.name  #consider command confusion (multiple potential options)
    
    if said == "quit":
        #function to prompt saving to text doc (call separate save function)
        QUIT()
        return False
    elif said == "look":
        LOOK(cmd, room, player)
    elif said == "go":
        GO(cmd, room, player, allRooms)
    elif said == "opens":
        pass
    elif said == "close":
        pass
    elif said == "take":
        pass
    elif said == "put":
        pass
    elif said == "use":
        pass
    elif said == "equip":
        pass
    elif said == "eat":
        pass
    elif said == "touch":
        pass
    else:
        print(Fore.RED + "I don't know what you're saying.")
        print(Style.RESET_ALL, end="", flush=True)
    return True


#TODO: implement saving feature, need to pass rooms and player
def QUIT():
    good = False
    while not good:
        ans = input("Would you like to save your progress? (y/n)\n>>> ").lower()
        if ans == "y":
            print("Saving...  ", end="")
            sleep(2)
            print("Feature not implemented.\n")  #Game saved
            good = True
        elid ans == "n":
            good = True


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
            
            elif quads[(player.roomLoc)] == Item:
                print("Not sure how you're looking at this.")
                #pass
            
            elif quads[(player.roomLoc)] == Interactable:
                print("Still need to design this.")
                #pass
            
            elif quads[(player.roomLoc)] == NPC:
                if quads[(player.roomLoc)].inventoryOpen:
                    print((quads[(player.roomLoc)].inventory).list_items)   #check if looking at NPCs items/inventory
                else:
                    print(quads[(player.roomLoc)].description)   #check if looking at NPC


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



#I don't think this incorporates doors (need to check is there is one, open/closed, locked)

def GO(cmd, room, player, allRooms):
    direction = cmd[1][0]  #sends first character of direction
    
    if len(cmd) < 2:
            #consider turning this into a function (pass text and color)
            print(Fore.RED + "Specify direction")
            print(Style.RESET_ALL, end="", flush=True)
            
    elif (direction == "n" or direction == "s" or direction == "e" or
          direction == "w" or direction == "u" or direction == "d"):
        location(direction, loc, allRooms)
    
    elif cmd[0] == "climb" or cmd[0] == "desend":
        print("Not implemented yet")  #TODO u and d are not ready either
    
    else:
        print(Fore.RED + "I'm not sure where that's at.")  #TODO add more
        print(Style.RESET_ALL, end="", flush=True)




def OPENS():
    pass  #set the roomLoc to the quadrant the box is in
















