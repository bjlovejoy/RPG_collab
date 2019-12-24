from colorama import Fore, Style


class Command:
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords

quit = Command("quit", ["quit", "exit", "end", "q"])

look = Command("look", ["look", "see", "study", "view", "check"])
go = Command("go", ["go", "walk", "run", "travel", "head", "leave"])
opens = Command("open", ["open", "enter"])
close = Command("close", ["close"])

take = Command("take", ["take", "grab"])
put = Command("put", ["put", "place"])

use = Command("use", ["use", "interact"])  #need to equip before using if equipable
equip = Command("equip", ["equip"])

eat = Command("eat", ["eat", "drink"])
touch = Command("touch", ["touch", "feel"])

#attack, fight, build, create, talk to, push, set, lay, place, drop, remove
#feel, cast, light, poop/pee, curse words, yell, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into)

allCmds = [quit, look, go, opens, close, take, put, use, equip, eat]



def parseCmd(cmd, room, player, loc):
    use = "None"
    for i in allCmds:
        for j in (i.keywords):
            if cmd[0] == j:
                use = i.name  #consider command confusion (multiple potential options)
    
    if use == "look":
        LOOK(cmd, room, player)
    elif use == "go":
        GO()
    elif use == "quit":
        #function to prompt saving to text doc (call separate save function)
        QUIT()
        return False
    else:
        print("I don't know what you're saying.")
    return True



def QUIT():
    


#for looking in chests or at specific objects in chest,
#consider positional attribute in room class for which
#quadrant the player is in (does not always have to apply
#(default to None)
def LOOK(cmd, room, player):
    if len(cmd) == 1:
        room.look()
    elif cmd[1] == "around" or cmd[1] == "room":
        room.look()
    elif cmd[1] == "at" ann len(cmd) > 2:
        for i in range(2):
            del cmd[0]
        a = " "
        item = a.join(cmd)
        



def GO(cmd, room, player):
    direction = cmd[1][0]  #sends first character of direction
    
    if len(cmd) < 2:
            #consider turning this into a function (pass text and color)
            print(Fore.RED + "Specify direction")
            print(Style.RESET_ALL, end="", flush=True)
            
    elif direction == "n" or direction == "s" or direction == "e" or direction == "w":
        location(direction, loc)
    
    else:
        print("I'm not sure where that's at.")  #TODO add more





















