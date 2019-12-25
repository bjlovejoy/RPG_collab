from colorama import Fore, Style
from boxes import *
from items import *

#TODO: style is door, trapdoor, ladder, stairs, transport (97 -> 197 up)
#      (for now, implement ladders and stairs as unlocked doors,
#       then make new class for verticle pathways)
#keyID must be sting to use for keys, riddles, etc. (None if no lock)
#description (about the door)
#locked is set to False as default
#cutscene (when opening door first time; save passing through for room)
class Door:
    def __init__(self, names, description, locked=False, keyID=None, cutscene="Default"):
        self.names = names
        self.description = description
        self.locked = locked
        self.keyID = keyID
        self.cutscene = cutscene
        
    def look(self):
        print(self.description)
    
    def changeLock(self, newID):
        self.keyID = newID
    
    def lock(self, des):    #For use by developer, not user
        self.locked = True
        print(des)          #prints text for when door locks (hard-coded)
        
    def unlock(self, key):  #requires the key ID to test door
        self.locked = False
        if key == keyID:
            if self.cutscene == "Default":  #FIXME put text in a list and access list number (randint(0,4))
                num = randint(1, 5)
                if num == 1:
                    print("You hear the lock faintly click and the door eases open.")
                elif num == 2:
                    print("The key slowly turns until the lock clicks open.")
                elif num == 3:
                    print("The door unlocks and easily swings open.")
                elif num == 4:
                    print("The key fits snuggly in the lock.  The door is open.")
                elif num == 5:
                    print("\"Click!\"  The door swings open.")
            else:
                print(self.cutscene)
        else:
            print("The key didn't work.  The door is still locked.")  #TODO add more responses and colors

#************************************************************************************

class Room:
    def __init__(self, num, Quadrant, description, cutscene=None):
        self.num = num  #not required, as rooms will be entered into list "allRooms" in order
        
        self.q0 = Quadrant[0]
        self.q1 = Quadrant[1]   #potential door
        self.q2 = Quadrant[2]
        self.q3 = Quadrant[3]   #potential door
        self.q4 = Quadrant[4]   #potential door
        self.q5 = Quadrant[5]
        self.q6 = Quadrant[6]   #potential door
        self.q7 = Quadrant[7]
        
        self.quads = Quadrant
        
        self.description = description
        self.cutscene = cutscene   #if cutscene != None, play
        self.firstEnter = True      #This is a new room that hasn't been entered yet
    
    def playCutscene(self):
        if self.firstEnter and self.cutscene != None:
            print(self.cutscene)
    
    def look(self):
        print(self.description)
    
    #search quadrants for items/doors, NPCs, boxes, etc.
    def findItem(self, item):
        multiple = 0
        for i in self.quads:
            if i != None:
                pass
                
#STILL NEEDS WORK ^^^^^^^

   
    
    def saveState(self):
        print(Fore.CYAN + "All rooms states saved to text document")
        print(Style.RESET_ALL, end="", flush=True)
    
    def restoreState(self):
        print(Fore.CYAN + "The current state of the room from last "\
              "session has been restored.")
        print(Style.RESET_ALL, end="", flush=True)


#******************************************************************

'''
template = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

Door("True", )  #unlocking doors automatically opens them
Box()
Table()
Desk()
Item()
'''



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
                Box(),
                None],
               "You are in a comfy bedroom.  The wooden floor is polished "\
               "clean, as is most of the room.  There is a small jewelry "\
               "box at the foot of a soft, fluffy bed, which is next to "\
               "what appears to be a desk.  There are two doors, one to "\
               "the north and one to the east.",
               "You begin to stir as you awaken from a deep sleep.  You feel "\
               "a cold sweat on your forehead and your vision is hazy.  "\
               "As you sit up, your vision clears and you start to make "\
               "sense of your surroundings.")

kitchen = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

foyer = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

closet = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")


allRooms = [bedroom, kitchen, None, None, None, None, None, None, None, None,
            foyer, closet, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None]


