from colorama import Fore, Style


class look(Command):
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
            
    def execute_center(self, cmd, player, room):

        short_cmd = self.remove_filler(cmd)
        search_room = False

        if len(short_cmd) == 1:
            room.describe()
        
        elif len(short_cmd) == 2:
            if short_cmd[1] == "inventory":       #consider (rather than len):   if "inventory" in cmd
                                            #if want to make multiple names for inventory, do player.inventory.names
                player.enter_inventory()            #TODO: set to -2
                player.inventory.list_inventory()   #TODO: create this too
            
            elif short_cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                search_room = True
                item = short_cmd[1]
        
        else:
            item = " ".join(short_cmd[1:])    #should be the item we're searching for
            search_room = True

        if search_room:

            result = room.find_match(item)  #TODO: search/print description here or in room class? (return list)
                             #could also make it return the quadrant if it exists (-1 if not?)

            if result == None:
                pass    #TODO: could not find it (randint pick)
            
            elif type(result) is str:
                pass    #TODO: there are multiple, please refine (randint pick)
            
            else:
                if type(result) is Box:
                    if any(i in cmd for i in ["in", "inside"]):
                        '''
                        if result.locked:
                            print("Cant' do that Starfox")
                        else:
                            result.list_contents()
                        '''
                        #TODO: send to open command instead
                        #(will handle locked stuff, just list_contents here)

                    else:
                        result.describe()
                
                elif type(result) is Table:
                    if "at" in cmd:
                        pass  #TODO: print table description
                    
                    elif any(i in cmd for i in ["on", "ontop", "top"]):
                        pass  #TODO: print table contents
                    
                    else:
                        pass  #TODO: print both, one after the other
                
                elif type(result) is Door:
                    pass  #DO NOT IMPLEMENT in other places - doors controlled from center (okay here since just looking)

                elif type(result) is NPC:
                    pass  # check if NPC's inventory is open
                          # check if in battle with NPC (look for weaknesses/hints/fighting style)
                
                else:
                    print("Should not be able to get here [end of LOOK]")


            #"look in chest" - should this be allowed (call open), or require player to open
            #(special circumstance, similar to look on table)
            #maybe give description of chest with allude to being open/locked (hint the player to use open/unlock cmd)














    def execute_inventory(self, cmd, player, room):
        pass  #If not found, print note about exiting inventory first
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
        pass

    def execute_door(self, cmd, player, room):
        pass