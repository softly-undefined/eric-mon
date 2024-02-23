class Tile:
    #also need to give what the interaction is! some way to battle
    #don't add the sprite here
    #
    #
    def __init__(self, is_ground=False, is_interactable=False, interact_text='', is_door=False, door_map=None, door_coords=None):#interact_text):
        self.is_ground = is_ground
        self.is_interactable = is_interactable
        self.interact_text = interact_text
        self.is_door = is_door
        self.door_map = door_map
        self.door_coords = door_coords
        #self.interact_text = interact_text
    
    def interact(self):
        if self.is_interactable:
            print(self.interact_text)
            
            return True
        return False
    