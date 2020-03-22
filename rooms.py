from colorama import Fore, Style
from boxes import *
from items import *



class Room:
    def __init__(self, num, Quadrant, description, cutscene=None):
        self.num = num  #not required, as rooms will be entered into list "allRooms" in order
        
        self.q0 = Quadrant[0]
        self.q1 = Quadrant[1]
        self.q2 = Quadrant[2]
        self.q3 = Quadrant[3]
        self.q4 = Quadrant[4]
        self.q5 = Quadrant[5]
        self.q6 = Quadrant[6]
        self.q7 = Quadrant[7]
        
        self.quads = Quadrant
        
        self.description = description
        self.cutscene = cutscene   #if cutscene != None, play
        self.firstEnter = True      #This is a new room that hasn't been entered yet
    
    def playCutscene(self):
        if self.firstEnter and self.cutscene != None:
            print(self.cutscene)
    
    def describe(self):
        print(self.description)
    
    #search quadrants for items/doors, NPCs, boxes, etc.
    #RETURNS item, not for modification (READ ONLY)
    #given "name" of item, not type (ex. chest, steel door)
    def find_match(self, item):
        
        num_results = 0
        result = None

        for q in self.quads:
            if q != None:
                for n in q.names:
                    if n == item:
                        result = q
                        num_results += 1
        
        if multiple <= 1:
            return result       #return object or None
        
        else:
            return "multiple"   #consider replacing with class containing name "multiple"

        #for look, this should be handled by look (make a more general function here)


    def find_match_quad(self, item):
        pass
        #make similar function to above, but return quadrant number
        #(0-7, -1 for no match, so cmd can edit it directly) - consider multiple and no match

   #make one more simply to test if the object exists (may not be useful)



    def saveState(self):
        print(Fore.CYAN + "All rooms states saved to text document")
        print(Style.RESET_ALL, end="", flush=True)
    
    def restoreState(self):
        print(Fore.CYAN + "The current state of the room from last "\
              "session has been restored.")
        print(Style.RESET_ALL, end="", flush=True)



