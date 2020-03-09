from colorama import Fore, Style


class look:
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
        self.filler_words = ["at", "in", "for", "the", "a", "an", "my", "his", "her"]  #put this in __init__
        #(consider making look a cmd class object and passing it to look function)
          #(then, command class can have function for parsing and searching for the right commands)

    def remove_filler(self, cmd):
        for word in filler_words:
            if word in cmd:
                cmd.remove(word)
    
    def execute_center(self, cmd, player, room):

        self.remove_filler(cmd)
        search_room = False

        if len(cmd) == 1:
            room.describe()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":
                player.enter_inventory()  #TODO: set to -2
                player.inventory.list_inventory()
            
            elif cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                search_room = True
                item = cmd[1]
        
        else:
            item = " ".join(cmd[1:])
            search_room = True

        if search_room:
            room.find(item)  #TODO: search/print description here or in room class?
            


    def execute_inventory(self, cmd, player, room):
        pass  #If not found, print note about exiting inventory first
    
    def execute_box(self, cmd, player, room):

        if len(cmd) == 1:
            room[player.roomLoc].list_contents()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":  #replcae this with self.allCmds, but search for all (if in allCmds(find inventory or like)
                player.inventory.list_inventory()  #TODO: make this function to print contents as list intead of sentence

            else:

            #search for item, enter inventory, etc.

    def execute_table(self):
        pass

    def execute_desk(self):
        pass  #Not implemented yet

    def execute_interactable(self):
        pass
    
    def execute_NPC(self):
        pass

    def execute_door(self):
        pass