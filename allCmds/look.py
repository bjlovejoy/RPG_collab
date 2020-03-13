from colorama import Fore, Style


class look(Command):
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
        
        #(consider making look a cmd class object and passing it to look function)
          #(then, command class can have function for parsing and searching for the right commands)
    
    def execute_center(self, cmd, player, room):

        self.remove_filler(cmd)
        search_room = False

        if len(cmd) == 1:
            room.describe()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":       #consider (rather than len):   if "inventory" in cmd
                                            #if want to make multiple names for inventory, do player.inventory.names
                player.enter_inventory()            #TODO: set to -2
                player.inventory.list_inventory()   #TODO: create this too
            
            elif cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                search_room = True
                item = cmd[1]
        
        else:
            item = " ".join(cmd[1:])    #should be the item we're searching for
            search_room = True

        if search_room:

            result = room.findMatch(item)  #TODO: search/print description here or in room class? (return list)
                             #could also make it return the quadrant if it exists (-1 if not?)

            if result == None:
                pass    #could not find it (make list of string and pick one)
            
            elif type(result) is str:
                pass    #there are multiple, please refine (list of responses to choose from)
            
            else:
                result.describe()    #should be door, box, NPC, etc
                #may need to enter newline here?



            #try to generalize this (check if it exists, return object and type)
            #(will need for take/put/etc - does item exist, then do a thing)
            #(make one for rooms, chests, inventory, etc.)


            #if multiple, return string
            #if none, return none
            #if box, door, etc, return entire object (may not work for take/put/modification - fine for printing description)
            #make point of checking object type first



    def execute_inventory(self, cmd, player, room):
        pass  #If not found, print note about exiting inventory first
              #should handle looking at equipped items here (alert player of this)
    
    def execute_box(self, cmd, player, room):

        if len(cmd) == 1:
            room[player.roomLoc].list_contents()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":  #replcae this with self.allCmds, but search for all (if in allCmds(find inventory or like)
                player.inventory.list_inventory()  #TODO: make this function to print contents as list intead of sentence

            else:

            #look inside, look inside box, look in chest, look at [item in chest]

            #search for item, enter inventory, etc.

    def execute_table(self, cmd, player, room):
        pass

    def execute_desk(self, cmd, player, room):
        pass  #Not implemented yet

    def execute_interactable(self, cmd, player, room):
        pass
    
    def execute_NPC(self, cmd, player, room):
        pass

    def execute_door(self, cmd, player, room):
        pass