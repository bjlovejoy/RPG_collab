from colorama import Fore, Style
from copy import copy       #TODO: need to apply this any where where modifying objects (ex. lists)
                            # lists have their own copy method

class Command:
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords

        self.cmd = ""
        self.short_cmd = ""

        self.filler_words = ["at", "in", "for", "the", "a", "an", "to", "my", "his", "her"]

    def set_cmd(self, cmd):
        # save cmd list as member variable (shallow copy)
        self.cmd = cmd.copy()

    def set_short_cmd(self):
        self.remove_filler()
        self.remove_cmd_keyword()

    def remove_filler(self, exceptions: list=[]]):

        self.short_cmd = self.cmd.copy()

        for word in self.filler_words:
            if word in cmd_minimal and word not in exceptions:
                cmd_minimal = cmd_minimal.remove(word)

        return cmd_minimal
    
    def remove_cmd_keyword(self):

        for k in self.keywords:
            if k in self.cmd:
                self.cmd.remove()

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
    look(["look", "see", "study", "view", "check"]),
    go(["go", "walk", "run", "travel", "head"]),
    opens(["open", "enter", "unlock"]),
    close(["close", "shut"]),
    take(["take", "grab"]),
    put(["put", "place"]),
    use(["use", "interact", "try"]),
    equip(["equip"]),
    eat(["eat", "drink"]),
    touch(["touch", "feel"]),
    
]

#attack, fight, build, create, talk to, push, set, lay, place, drop, remove
#feel, cast, light, poop/pee, curse words, yell, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into)




#here, cmd is the full string of user input
def parseCmd(cmd, player, room):

    #first need to determine which command it is
        #if not legit, check object specific commands -> pass to player location
        #if potentially multiple commands, must differentiate -> pass to player location (try to avoid)
    


    #then, determine which part of room
    #(if in between center and box, indicate so and allow pass to both)

    determined_cmd.set_cmd = cmd.copy()
    determined_cmd.get_short_cmd()

    if player.roomLoc == -1:
        determined_cmd.execute_center(determined_cmd, player, room)
    
    elif player.roomLoc == -2:
        determined_cmd.execute_inventory()
    
    else:
        quadType = type(room[player.roomLoc])
        
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












#if trying to open chest in room from inventory, print, "no chest to open, if trying to open something in the room
#first exit inventory using 'exit (leave) inventory' command"
