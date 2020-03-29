from commands import Command

class command(Command):
    def __init__(self, keywords):
        self.name = keywords[0]
        self.keywords = keywords
    
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