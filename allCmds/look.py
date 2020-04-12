from colorama import Fore, Style
from commands import Command

'''
Colored text:

print(Fore.RED + "I don't know what you're saying.")
print(Style.RESET_ALL, end="", flush=True)
'''

class look(Command):
    def __init__(self, keywords):
        super().__init__(keywords)

    def execute_center(self, player, room):
        
        search_room = False

        if not self.short_cmd or any(i in self.short_cmd for i in ["here", "around", "room"]):
            room.describe()
        
        elif "inventory" in self.short_cmd:
            player.enter_inventory()
            player.inventory.list_contents()
        
        elif "stats" in self.short_cmd:
            player.show_stats()
            
        else:
            search_room = True
            item = " ".join(self.short_cmd)

        if search_room:

            result = room.find_match(item)

            if result == None:
                print("Not sure what you're looking at.")
                #TODO: could not find it (randint pick)
            
            elif type(result) is str:
                print("Multiple objects detected.  Please refine.")
                #TODO: there are multiple, please refine (randint pick)
            
            else:
                if type(result) is Box:
                    if any(i in self.cmd for i in ["in", "inside"]):
                        pass
                        #TODO: send to open command instead
                        #(will handle locked stuff, make open command auto print what's inside)
                        
                        #maybe give description of chest with allude to being open/locked/closed
                        #(hint the player to use open/unlock cmd)

                    else:
                        result.describe()
                
                elif type(result) is Table:
                    if "at" in self.cmd:
                        result.describe()  #print table description
                    
                    elif any(i in self.cmd for i in ["on", "ontop", "top"]):
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

    def execute_inventory(self, player, room):

        if not self.short_cmd:
            player.inventory.list_inventory()
        
        else:
            item = " ".join(self.short_cmd)
            result = player.inventory.search_inventory(item)  #TODO: make this like room.find_match (rename to search?)

            if result is None:
                pass #If not found, print note about exiting inventory first
                #say, "I don't see that in your inventory"

            elif type(result) is str:
                pass  #multiple returns

            else:
                result.describe()
            
            #equipped items will be in inventory with tag (ex. shoes (equipped) )
            #consider suggestsions (look health - "did you mean health cmd?")
    
    def execute_box(self, player, room):

        if not self.short_cmd:
            room[player.room_loc].list_contents()
        
        elif "inventory" in self.short_cmd:
            player.inventory.list_inventory()  #TODO: make this function to print contents as list intead of sentence
            # when in inventory, if you leave, must return to inside box

        else:

        #look inside, look inside box, look in chest, look at [item in chest]

        #can also still look "at" chest

        #search for item, enter inventory, etc.

    def execute_table(self, player, room):
        pass

    def execute_desk(self, player, room):
        pass  #Not implemented yet

    def execute_interactable(self, player, room):
        pass  #Not implemented yet
    
    def execute_NPC(self, player, room):
        pass  # check if NPC's inventory is open

    def execute_door(self, player, room):
        pass
        #TODO: determine if player should be in door quad (consider setting to quad, but if
        #      the player does not interact with the door on their next turn, reset pos to center)