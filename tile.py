# a Tile defines the contents of a location on the grid.
# It has a number of attributes, and subclasses like Sign and Door
# defining a specific set of attributes
#
#
#
#

class Tile:
    #
    # Need support for battles
    #
    def __init__(self, is_ground=False, is_interactable=False, interact_text='', is_door=False, door_map=None, door_coords=None, is_sprite=False):#interact_text):
        self.is_ground = is_ground

        #specific to objects that will be interactable with "i" click
        self.is_interactable = is_interactable
        self.interact_text = interact_text

        #specific to door objects
        self.is_door = is_door
        self.door_map = door_map
        self.door_coords = door_coords


        self.is_sprite = is_sprite


class Sign(Tile):
    def __init__(self, text):
        super().__init__(is_interactable=True, interact_text=text)

class Door(Tile):
    def __init__(self, travel_to, coords):
        super().__init__(is_door=True, is_ground=True, door_map=travel_to, door_coords=coords)