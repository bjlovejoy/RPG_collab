from commands import Command

class command(Command):
    def __init__(self):
        #if wish to pass more, pass everything and call super or Command.__init__(self, vars)
        #(super is good for single inheritance)
        #Otherwise, remove __init__ (or keep and add Command.__init__ to everything)
    
    def execute_center(self, cmd, player, room):
        pass

    def execute_inventory(self, cmd, player, room):
        pass
    
    def execute_box(self, cmd, player, room):
        pass
    
    def execute_table(self, cmd, player, room):
        pass
    
    def execute_desk(self, cmd, player, room):
        pass  #Not implemented yet

    def execute_interactable(self, cmd, player, room):
        pass  #Not implemented yet

    def execute_NPC(self, cmd, player, room):
        pass

    def execute_door(self, cmd, player, room):
        pass