from colorama import Fore, Style

#Template (not worth doing super().__init__(self, etc.) )
"""
class Command:
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
    
    def execute_center(self, cmd, room, player):
        pass

    def execute_inventory(self, cmd, room, player):
        pass
    
    def execute_box(self, cmd, room, player):
        pass
    
    def execute_table():
        pass
    
    def execute_desk():
        pass  #Not implemented yet

    def execute_interactable(self, cmd, room, player):
        pass

    def execute_NPC(self, cmd, room, player):
        pass

    def execute_door(self, cmd, room, player):
        pass
"""

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
def parseCmd(cmd, room, player):

    #first, determine which command it is
        #if not legit, check object specific commands -> pass to player location
        #if potentially multiple commands, must differentiate -> pass to player location (try to avoid)

    #then, determine which part of room
    #(if in between center and box, indicate so and allow pass to both)

    quadType = type(room[player.roomLoc])

    if player.roomLoc == -1:
        determined_cmd.execute_center()
    
    elif player.roomLoc == -2:
        pass
    
    #New if block in case in between center and box?
    
    if quadType is Box:
        pass

    elif quadType is Table:
        pass

    elif quadType is Desk:
        pass  #Not implemented yet

    elif quadType is Interactable:
        pass

    elif quadType is NPC:
        pass

    elif quadType is Door:
        pass
    
    else





#make parsing commands either a tight loop using a list of commands or allow
#all commands to execute the same way (ex. cmd.execute())








#if trying to open chest in room from inventory, print, "no chest to open, if trying to open something in the room
#first exit inventory using 'exit (leave) inventory' command"
