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

use = Command("use", ["use"])  #need to equip before using if equipable
equip = Command("equip", ["equip"])

eat = Command("eat", ["eat", "drink"])


#attack, fight, build, create, talk to, interact, push, touch
#grab, feel, cast, light, poop/pee, curse words, yell, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into), place
#set, lay

allCmds = [quit, look, go, opens, close, take, put, use, equip, eat]



def parseCmd(cmd):
    use = "None"
    for i in allCmds:
        for j in (i.keywords):
            if cmd[0] == j:
                use = i.name
    
    #consider making command function in commands.py
    if use == "look":
        print("1")
    elif use == "go":
        if len(cmd) < 2:
            #consider turning this into a function (pass text and color)
            print(Fore.RED + "Specify direction")
            print(Style.RESET_ALL, end="", flush=True)
        else:
            location(cmd[1], loc)
    elif use == "quit":
        playing = False
    else:
        print("I don't know what you're saying.")




