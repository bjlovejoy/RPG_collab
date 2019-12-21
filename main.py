#from playsound import playsound
from colorama import Fore, Style
#user (yellow), error (red), updates/system message (cyan)
#NPCs and characters (green)

from random import randint
from rooms import *
from boxes import *
from commands import *
from player import *
from items import *


loc = 3  #starting location
playing = True

#consider making function for this
"""
validSelection = False
menuSelect = input("\nPlease Select from Below:\n\n\
1) New Game\n\
2) Load Game\n\
3) Help\n\
4) Quit\n\n"\
+ Fore.YELLOW + ">>> ")
print(Style.RESET_ALL, end="", flush=True)

while(not validSelection):
    if str.isnumeric(menuSelect):
        menuSelect = int(menuSelect)
        if menuSelect < 1 or menuSelect > 4:
            print(Fore.RED + "Invalid Selection")
            print(Style.RESET_ALL, end="", flush=True)
            menuSelect = input(Fore.YELLOW + ">>> ")
            print(Style.RESET_ALL, end="", flush=True)
        else:
            validSelection = True
    else:
        print(Fore.RED + "Invalid Selection")
        print(Style.RESET_ALL, end="", flush=True)
        menuSelect = input(Fore.YELLOW + ">>> ")
        print(Style.RESET_ALL, end="", flush=True)


if menuSelect == 1:    #New Game
    createPlayer()
elif menuSelect == 2:  #Load Game
    for i in allRooms:
        i.restoreState()
elif menuSelect == 3:  #Help
    print("Help manual displayed.")
elif menuSelect == 4:  #Quit
    playing = False
"""


#Testing area (make functions handle \n, not in literals)
allRooms[0].q5.look()
print("")
allRooms[0].q3.list_items()
allRooms[0].q3.remove_all()
print("")
allRooms[0].q3.list_items()


while(playing):
    cmd = (input(Fore.YELLOW + ">>> ").lower()).split()
    print(Style.RESET_ALL, end="", flush=True)
    
    parseCmd(cmd)
    


print("\nUntil next time adventurer...\n\n\n")









