from colorama import Fore, Style


def createPlayer():
    print("Player created")





#see notebook for additional player attributes
class Player:
    def __init__(self, name):
        self.name = name



#consider location as player method
def location(direction, loc):
    if direction == "n" and loc < 90:
        loc += 10
    elif direction == "s" and loc > 9:
        loc -= 10
    elif direction == "e" and loc % 10 != 9:
        loc += 1
    elif direction == "w" and loc % 10 != 0:
        loc -= 1
