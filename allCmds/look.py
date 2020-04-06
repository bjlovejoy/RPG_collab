from colorama import Fore, Style
from commands import Command

'''
Colored text:

print(Fore.RED + "I don't know what you're saying.")
print(Style.RESET_ALL, end="", flush=True)
'''

class look(Command):
    def __init__(self):
        pass

    def execute_center(self, cmd, player, room):
        
        search_room = False

        if len(self.short_cmd) == 1:
            room.describe()
        
        elif len(self.short_cmd) == 2:
            if self.short_cmd[1] == "inventory":
                    #consider (rather than len):   if "inventory" in cmd
                    #if want to make multiple names for inventory, do player.inventory.names
                player.enter_inventory()            #TODO: set to -2
                player.inventory.list_inventory()   #TODO: create this too
            
            elif self.short_cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                search_room = True
                item = self.short_cmd[1]
        
        else:

            if "inventory" in self.short_cmd:
                    #if want to make multiple names for inventory, do player.inventory.names
                player.enter_inventory()            #TODO: set to -2
                player.inventory.list_inventory()   #TODO: create this too
            
            else:
                search_room = True
                item = " ".join(self.short_cmd[1:])    #should be the item we're searching for

        if search_room:

            result = room.find_match(item)
                #TODO: search/print description here or in room class? (return list)
                #could also make it return the quadrant if it exists (-1 if not?)

            if result == None:
                print("Not sure what you're looking at.")
                #TODO: could not find it (randint pick)
            
            elif type(result) is str:
                print("Multiple objects detected.  Please refine.")
                #TODO: there are multiple, please refine (randint pick)
            
            else:
                if type(result) is Box:
                    if any(i in cmd for i in ["in", "inside"]):
                        pass
                        #TODO: send to open command instead
                        #(will handle locked stuff, make open command auto print what's inside)
                        
                        #maybe give description of chest with allude to being open/locked/closed
                        #(hint the player to use open/unlock cmd)

                    else:
                        result.describe()
                
                elif type(result) is Table:
                    if "at" in cmd:
                        result.describe()  #print table description
                    
                    elif any(i in cmd for i in ["on", "ontop", "top"]):
                        result.list_contents()  #print table contents
                    
                    else:
                        result.describe()
                        result.list_contents()
                        #print both, one after the other
                
                elif type(result) is Door:
                    result.describe()

                elif type(result) is NPC:

                    result.describe()

                    #TODO: check if in battle with NPC (look for weaknesses/hints/fighting style)
                    #TODO: consider redoing describe to take parameters/lists of descriptions
                    #look at items the NPC is wearing (maybe handle below in NPC look category)
                
                else:
                    print("Should not be able to get here [end of LOOK]")













    def execute_inventory(self, cmd, player, room):

        
        #If not found, print note about exiting inventory first
        #should handle looking at equipped items here (alert player of this)

        #consider suggestsions (look health - "did you mean health cmd?")
    
    def execute_box(self, cmd, player, room):

        if len(cmd) == 1:
            room[player.roomLoc].list_contents()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":  #replcae this with self.allCmds, but search for all (if in allCmds(find inventory or like)
                player.inventory.list_inventory()  #TODO: make this function to print contents as list intead of sentence

            else:

            #look inside, look inside box, look in chest, look at [item in chest]

            #can also still look "at" chest

            #search for item, enter inventory, etc.

    def execute_table(self, cmd, player, room):
        pass

    def execute_desk(self, cmd, player, room):
        pass  #Not implemented yet

    def execute_interactable(self, cmd, player, room):
        pass  #Not implemented yet
    
    def execute_NPC(self, cmd, player, room):
        pass  # check if NPC's inventory is open

    def execute_door(self, cmd, player, room):
        pass
        #TODO: determine if player should be in door quad (consider setting to quad, but if
        #      the player does not interact with the door on their next turn, reset pos to center)