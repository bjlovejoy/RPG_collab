from colorama import Fore, Style


class Command:
    def __init__(self, names):
        self.name = names[0]
        self.keywords = names
    
    def execute_center(self):
        pass

    def execute_inventory(self):
        pass
    
    def execute_box(self):
        pass

    def execute_door(self):
        pass

    def execute_character(self):
        pass

    def execute_interactable(self):
        pass



#here, cmd is the full string of user input
def parseCmd(cmd, room, player):

    #first, determine which command it is
        #if not legit, check object specific commands -> pass to player location
        #if potentially multiple commands, must differentiate -> pass to player location (try to avoid)

    #then, determine which room

    if player.loc == -1:



#make parsing commands either a tight loop using a list of commands or allow
#all commands to execute the same way (ex. cmd.execute())

#consider determining player location before hand, and enter the right function
#(thus, all commands will have multiple execution functions based on location)

class look(Command):
    def __init__(self):
        super?




#if trying to open chest in room from inventory, print, "no chest to open, if trying to open something in the room
#first exit inventory using 'exit (leave) inventory' command"
