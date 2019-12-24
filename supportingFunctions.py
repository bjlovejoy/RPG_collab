


"""
validSelection = False
menuSelect = input("\nPlease Select from Below:\n\n\
1) New Game\n\
2) Load Game\n\
3) Help\n\
4) Quit\n\n"\
+ Fore.YELLOW + ">>> ")
print(Style.RESET_ALL, end="", flush=True)

while(not validSelection):
    if str.isnumeric(menuSelect):
        menuSelect = int(menuSelect)
        if menuSelect < 1 or menuSelect > 4:
            print(Fore.RED + "Invalid Selection")
            print(Style.RESET_ALL, end="", flush=True)
            menuSelect = input(Fore.YELLOW + ">>> ")
            print(Style.RESET_ALL, end="", flush=True)
        else:
            validSelection = True
    else:
        print(Fore.RED + "Invalid Selection")
        print(Style.RESET_ALL, end="", flush=True)
        menuSelect = input(Fore.YELLOW + ">>> ")
        print(Style.RESET_ALL, end="", flush=True)


if menuSelect == 1:    #New Game
    createPlayer()
elif menuSelect == 2:  #Load Game
    for i in allRooms:
        i.restoreState()
elif menuSelect == 3:  #Help
    print("Help manual displayed.")
elif menuSelect == 4:  #Quit
    playing = False
"""


