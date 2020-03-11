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
            if cmd[1] == "inventory":
                player.enter_inventory()            #TODO: set to -2
                player.inventory.list_inventory()   #TODO: create this too
            
            elif cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                search_room = True
                item = cmd[1]
        
        else:
            item = " ".join(cmd[1:])
            search_room = True

        if search_room:
            room.find(item)  #TODO: search/print description here or in room class? (return list)



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