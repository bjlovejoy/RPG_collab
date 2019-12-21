
#can use local, nonlocal and global to reference variables
#local - only within function
#nonlocal - outside of function
#global - completely different object outside of function

from colorama import Fore, Style
from boxes import *
from items import *

#style is door, trapdoor, ladder, stairs, transport (else, 
#default material is wood
class Door:
    def __init__(self, locked="False", style="door", material="wood"):
        self.locked = locked
        self.style = style
        self.material = material

class Room:
    def __init__(self, num, Quadrant, description, cutscene=None):
        self.q0 = Quadrant[0]
        self.q1 = Quadrant[1]   #potential door
        self.q2 = Quadrant[2]
        self.q3 = Quadrant[3]   #potential door
        self.q4 = Quadrant[4]   #potential door
        self.q5 = Quadrant[5]
        self.q6 = Quadrant[6]   #potential door
        self.q7 = Quadrant[7]
        self.description = description
        self.cutscene = cutscene   #if cutscene != None, play
        self.firstTime = True      #This is a new room that hasn't been entered yet
    def playCutscene(self):
        if self.firstTime and self.cutscene != None:
            print(self.cutscene)
    def look(self):
        print(self.description)
    def saveState(self):
        print("All rooms states saved to text document")
    def restoreState(self):
        print(Fore.CYAN + "The current state of the room from last "\
              "session has been restored.")
        print(Style.RESET_ALL, end="", flush=True)


#******************************************************************


bedroom = Room(0, 
               [None,
                Door(True),
                None,
                Box(["jewelry box", "jewelrybox", "jewelry"],
                    [Item(["key", "home key", "home"], "a small, polished, silver key with the "\
                          "inscription, \"Home\""),
                    Item(["ring", "gold ring"], "an old gold ring, not worth very much")],
                    False, 3),
                Door(True),
                Item("Bed", "It looks warm with fluffy pillows and blankets."\
                     "  You feel like you could sleep in it for years."),
                None,
                None],
               "You are in a comfy bedroom.  The wooden floor is polished "\
               "clean, as is most of the room.  There is a small jewelry "\
               "box at the foot of a soft, fluffy bed and two doors.  One to "\
               "the north and one to the east.",
               "You begin to stir as you awaken from a deep sleep.  You feel "\
               "a cold sweat on your forehead and your vision is hazy.  "\
               "As you sit up, your vision clears and you start to make "\
               "sense of your surroundings.")

#kitchen = 

#foyer = 

#closet = 


allRooms = [bedroom]


