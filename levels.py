'''
template = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

Door("True", )  #unlocking doors automatically opens them
Box()
Table()
Desk()
Item()
'''



bedroom = Room(0, 
               [None,
                Door(True),
                None,
                Box(["jewelry box", "jewelrybox", "jewelry"],
                    [Item(["key", "home key", "home"], "a small, polished, silver key with the "\
                          "inscription, \"Home\""),
                    Item(["gold ring", "ring"], "an old gold ring, not worth very much")],
                    False, 3),
                Door(True),
                Item("Bed", "It looks warm with fluffy pillows and blankets."\
                     "  You feel like you could sleep in it for years."),
                Box(),
                None],
               "You are in a comfy bedroom.  The wooden floor is polished "\
               "clean, as is most of the room.  There is a small jewelry "\
               "box at the foot of a soft, fluffy bed, which is next to "\
               "what appears to be a desk.  There are two doors, one to "\
               "the north and one to the east.",
               "You begin to stir as you awaken from a deep sleep.  You feel "\
               "a cold sweat on your forehead and your vision is hazy.  "\
               "As you sit up, your vision clears and you start to make "\
               "sense of your surroundings.")

kitchen = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

foyer = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")

closet = Room(0,
                [None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None],
                ""\
                "",
                ""\
                "")


allRooms = [bedroom, kitchen, None, None, None, None, None, None, None, None,
            foyer, closet, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None,
            None, None, None, None, None, None, None, None, None, None]
