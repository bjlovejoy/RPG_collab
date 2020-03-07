
#TODO: link room and cmd to player so I only have to pass player


class look:
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
        self.filler_words = ["at", "in", "for", "the", "a", "an"]  #put this in __init__
        #(consider making look a cmd class object and passing it to look function)
          #(then, command class can have function for parsing and searching for the right commands)

    def remove_filler(self, cmd):
        for word in filler_words:
            if word in cmd:
                cmd.remove(word)
    
    def execute_center(self, cmd, player, room):

        self.remove_filler(cmd)

        if len(cmd) == 1:
            room.describe()
        
        elif len(cmd) == 2:
            if cmd[1] == "inventory":
                player.inventory.list_inventory()
            
            elif cmd[1] in ["here", "around", "room"]:
                room.describe()
            
            else:
                check_room  #

    def execute_inventory(self, cmd, player, room):
        pass
    
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