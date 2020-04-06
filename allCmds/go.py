


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