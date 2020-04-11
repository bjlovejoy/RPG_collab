from commands import Command

class command(Command):
    def __init__(self, keywords):
        super().__init__(keywords)   #could also use Command. (but need self as arg)

        #if wish to pass more, pass everything and call super or Command.__init__(self, vars)
        #(super is good for single inheritance)
        #Otherwise, remove __init__ (or keep and add Command.__init__ to everything)
    
    def execute_center(self, player, room):
        pass

    def execute_inventory(self, player, room):
        pass
    
    def execute_box(self, player, room):
        pass
    
    def execute_table(self, player, room):
        pass
    
    def execute_desk(self, player, room):
        pass  #Not implemented yet

    def execute_interactable(self, player, room):
        pass  #Not implemented yet

    def execute_NPC(self, player, room):
        pass

    def execute_door(self, cmd, player, room):
        pass