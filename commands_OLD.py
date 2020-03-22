from colorama import Fore, Style


    print(Fore.RED + "I don't know what you're saying.")
    print(Style.RESET_ALL, end="", flush=True)





#TODO: implement saving feature, need to pass rooms and player
def QUIT():
    good = False
    while not good:
        ans = input("Would you like to save your progress? (y/n)\n>>> ").lower()
        if ans == "y":
            print("Saving...  ", end="")
            sleep(2)
            print("Feature not implemented.\n")  #Game saved
            good = True
        elid ans == "n":
            good = True

















#I don't think this incorporates doors (need to check is there is one, open/closed, locked)

def GO(cmd, room, player, allRooms):
    direction = cmd[1][0]  #sends first character of direction
    
    if len(cmd) < 2:
            #consider turning this into a function (pass text and color)
            print(Fore.RED + "Specify direction")
            print(Style.RESET_ALL, end="", flush=True)
            
    elif (direction == "n" or direction == "s" or direction == "e" or
          direction == "w" or direction == "u" or direction == "d"):
        location(direction, loc, allRooms)
    
    elif cmd[0] == "climb" or cmd[0] == "desend":
        print("Not implemented yet")  #TODO u and d are not ready either
    
    else:
        print(Fore.RED + "I'm not sure where that's at.")  #TODO add more
        print(Style.RESET_ALL, end="", flush=True)




def OPENS():
    pass  #set the roomLoc to the quadrant the box is in
















