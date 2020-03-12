from colorama import Fore, Style

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