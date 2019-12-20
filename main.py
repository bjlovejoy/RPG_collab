#from playsound import playsound
from colorama import Fore, Style
from random import randint
from room import *
from command import *
from player import *


loc = 3  #starting location
    
createPlayer()


def location(direction, loc):
    if direction == "n" and loc < 90:
        loc += 10
    elif direction == "s" and loc > 9:
        loc -= 10
    elif direction == "e" and loc % 10 != 9:
        loc += 1
    elif direction == "w" and loc % 10 != 0:
        loc -= 1







playing = True
while(playing):
    cmd = (input(">>> ").lower()).split()
    
    use = "Nonsense"
    for i in allCmds:
        for j in (i.keywords):
            if cmd[0] == j:
                use = i.name
    
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

print("\nUntil next time adventurer...\n\n\n")









