


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