#can use local, nonlocal and global to reference variables
#local - only within function
#nonlocal - outside of function
#global - completely different object outside of function


from playsound import playsound
from colorama import Fore, Style
#user (yellow), error (red), updates/system message (cyan)
#NPCs and characters (green)

from random import randint
from rooms import *
from boxes import *
from commands import *
from characters import *
from items import *


loc = 0         #starting location
playing = True  #main loop bool


#***********************************************************

#Testing area (make functions handle \n, not in literals)
#allRooms[0].q5.look()
#print("")
#allRooms[0].q3.list_items()
#allRooms[0].q3.remove_all()
#print("")
#allRooms[0].q3.list_items()

#***********************************************************


while(playing):
    cmd = (input(Fore.YELLOW + ">>> ").lower()).split()
    print(Style.RESET_ALL, end="", flush=True)
    
    playing = parseCmd(cmd, room, player, loc)


print("\nUntil next time adventurer...\n")  #Add 2 more \n


#TODO consider rooms where you want the cutscene to play even after the first time,
#     or different room/door entrance text for different doors into the room






