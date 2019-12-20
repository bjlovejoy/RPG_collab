
#can use local, nonlocal and global to reference variables
#local - only within function
#nonlocal - outside of function
#global - completely different object outside of function

from boxes import *

#style is door, trapdoor, ladder, stairs, transport (else, 
#default material is wood
class Door:
    def __init__(self, locked, style="door", material="wood"):
        self.style = style
        self.locked = locked
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
    def saveState():
        print("All rooms states saved to text document")
        
#******************************************************************


bedroom = Room(0, 
               [None,
                Door(),
                None,
                Box(),
                Door(),
                Item("Bed"),
                None,
                None],
               "You are in a comfy bedroom.  The wooden floor is polished
               clean, as is most of the room.  There is a small jewlery
               box at the foot of a soft, fluffy bed and two doors.  One to
               the north and one to the east.\n",
               "You begin to stir as you awaken from a deep sleep.  You feel
               a cold sweat on your forehead and your vision is hazy.  As you
               sit up, your vision clears and you start to make sense of your surroundings.\n")

kitchen = 

foyer = 

closet = 


allRooms = [room1, room2, room3, room4]


