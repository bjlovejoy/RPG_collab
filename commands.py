from colorama import Fore, Style
from copy import copy       #TODO: need to apply this any where where modifying objects (ex. lists)
                            # lists have their own copy method

class Command:
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords

        self.cmd = ""
        self.short_cmd = ""

        self.filler_words = ["at", "in", "inside", "over", "for", "the", "a", "an", "to", "my", "his", "her"]

    def set_cmds(self, cmd):
        self.cmd       = cmd.copy()
        self.short_cmd = cmd.copy()

        for word in self.short_cmd:
            if ((word in self.filler_words) or (word in self.keywords)) and word not in exceptions:
                self.short_cmd.remove(word)
    
    def clear_cmds(self):
        self.cmd.clear()
        self.short_cmd.clear()
            
    def get_short_cmd(self, exceptions: list=[]):
        short_cmd = self.cmd.copy()

        for word in short_cmd:
            if ((word in self.filler_words) or (word in self.keywords)) and word not in exceptions:
                short_cmd.remove(word)
        
        return short_cmd

    def execute_center(self, cmd, player, room):
        raise NotImplementedError

    def execute_inventory(self, cmd, player, room):
        raise NotImplementedError
    
    def execute_box(self, cmd, player, room):
        raise NotImplementedError
    
    def execute_table(self, cmd, player, room):
        raise NotImplementedError
    
    def execute_desk(self, cmd, player, room):
        raise NotImplementedError  #Not implemented yet

    def execute_interactable(self, cmd, player, room):
        raise NotImplementedError  #Not implemented yet

    def execute_NPC(self, cmd, player, room):
        raise NotImplementedError

    def execute_door(self, cmd, player, room):
        raise NotImplementedError

#initialize all command objects in a list to be referenced in parseCmd below
allCmds = [
    look(["look", "see", "study", "view", "check", "search"]),
    go(["go", "walk", "run", "travel", "head"]),
    opens(["open", "enter", "unlock"]),
    close(["close", "shut"]),
    take(["take", "grab"]),
    put(["put", "place"]),
    use(["use", "interact", "try"]),
    equip(["equip"])
]

#attack, fight, build, create, talk to (say, yell?), push, set, lay, place, drop, remove
#cast, light, poop/pee/fart, curse words, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into)
    #eat(["eat", "drink"])
    #touch(["touch", "feel"]) - interact



#here, cmd is the full string of user input
def parseCmd(cmd, player, room):

    #first need to determine which command it is
        #if not legit, check object specific commands -> pass to player location
        #if potentially multiple commands, must differentiate -> pass to player location (try to avoid)
    


    #then, determine which part of room
    #(if in between center and box, indicate so and allow pass to both)

    determined_cmd.set_cmds(cmd)

    if player.room_loc == -1:
        determined_cmd.execute_center(determined_cmd, player, room)
    
    elif player.room_loc == -2:
        determined_cmd.execute_inventory()
    
    else:
        quadType = type(room[player.room_loc])
        
        if quadType is Box:
            determined_cmd.execute_box()

        elif quadType is Table:
            determined_cmd.execute_table()

        elif quadType is Desk:
            determined_cmd.execute_desk()           #Not implemented yet

        elif quadType is Interactable:
            determined_cmd.execute_interactable()   #Not implemented yet

        elif quadType is NPC:
            determined_cmd.execute_NPC()

        elif quadType is Door:
            determined_cmd.execute_door()
        
        else
            pass  #empty space (None type or other)

    determined_cmd.clear_cmds()










#if trying to open chest in room from inventory, print, "no chest to open, if trying to open something in the room
#first exit inventory using 'exit (leave) inventory' command"
