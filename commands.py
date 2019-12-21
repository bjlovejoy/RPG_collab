class Command:
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords


look = Command("look", ["look", "see", "study", "view", "check"])
go = Command("go", ["go", "walk", "run", "travel", "head", "leave"])
take = Command("take", ["take", "grab"])
use = Command("use", ["use"])  #need to equip before using if equipable
equip = Command("equip", ["equip"])
opens = Command("open", ["open", "enter"])
close = Command("close", ["close"])
eat = Command("eat", ["eat", "drink"])
quit = Command("quit", ["quit", "exit", "end", "q"])

#attack, fight, build, create, talk to, interact, push, touch
#grab, feel, cast, light, poop/pee, curse words, yell, break (strength checks),
#activate, turn on, turn off, flip (switch), leave, rest (sleep), put (into), place
#set, lay

allCmds = [look, go, take, use, equip, opens, eat, quit]
