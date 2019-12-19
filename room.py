
#can use local, nonlocal and global to reference variables
#local - only within function
#nonlocal - outside of function
#global - completely different object outside of function

from boxes import *

#style is door, trapdoor, ladder, stairs, transport (else, 
#default material is wood
class Door:
    def __init__(self, style="door", locked, material="wood"):
        self.style = style
        self.locked = locked
        self.material = material

class Wall:
    def __init__(self, material, description)
    self.material = material
    self.description = description

class Room:
    def __init__(self, Quadrant, description):
        #q0 is reserved for player space
        self.q0 = Quadrant[0]
        self.q1 = Quadrant[1]
        self.q2 = Quadrant[2]   #potential door
        self.q3 = Quadrant[3]
        self.q4 = Quadrant[4]   #potential door
        self.q5 = Quadrant[5]
        self.q6 = Quadrant[6]   #potential door
        self.q7 = Quadrant[7]
        self.q8 = Quadrant[8]   #potential door
        self.description = description
        




