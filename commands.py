from colorama import Fore, Style

class Command:
    self.filler_words = ["at", "in", "for", "the", "a", "an", "to", "my", "his", "her"]

    def remove_filler(self, cmd, exceptions: list=[]]):

        cmd_minimal = cmd

        for word in self.filler_words:
            if word in cmd_minimal and word not in exceptions:
                cmd_minimal = cmd_minimal.remove(word)

        return cmd_minimal

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


    if player.roomLoc == -1:
        determined_cmd.execute_center()
    
    elif player.roomLoc == -2:
        determined_cmd.execute_inventory()
    
    else:
        quadType = type(room[player.roomLoc])
    
    #New if block in case in between center and box?
    
        if quadType is Box:
            determined_cmd.execute_box()

        elif quadType is Table:
            determined_cmd.execute_table()

        elif quadType is Desk:
            determined_cmd.execute_desk()  #Not implemented yet

        elif quadType is Interactable:
            determined_cmd.execute_interactable()

        elif quadType is NPC:
            determined_cmd.execute_NPC()

        elif quadType is Door:
            determined_cmd.execute_door()
        
        else
            pass  #empty space (None type or other)












#if trying to open chest in room from inventory, print, "no chest to open, if trying to open something in the room
#first exit inventory using 'exit (leave) inventory' command"