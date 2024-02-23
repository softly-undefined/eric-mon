from tile import Tile
import maps
import settings

# every different sprite is a new "code" (g is a code, x is a code)
# how to integrate npc's into this? must have their own codes (how to make them turn and stuff)
#
# to do the calculation of where the player should ge placed onto a new map im thinking of making a linked list to do it
# like a sorta map thing ? future thing prog
#
# really need to make this into a class

map_list=[]

def read_map(map_name):
    map = None
    for item in map_list:
        if item.name == map_name:
            map = item
    obj_map = Map(map.name, map.grid)
    for row_index, row in enumerate(map.grid):
        for col_index, col in enumerate(row):
            if isinstance(col, str):
                if col == 'x': #basic wall tile
                    obj_map.grid[row_index][col_index] = Tile(is_ground=False)
                elif col == 'g': #basic ground tile
                    obj_map.grid[row_index][col_index] = Tile(is_ground=True)
            if isinstance(col, Tile):
                obj_map.grid[row_index][col_index] = col

    return obj_map

class Map:
    def __init__(self, name='', grid=None):
        self.name = name
        self.grid = grid

    
map_list.append(Map(name="TEST_MAP", grid=
[
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',Tile(is_interactable= True, interact_text="Second sign test!"),'g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g',Tile(is_ground=False, is_interactable=True, interact_text="test number 3"),'g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','x','x','x','x','x','x','g','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','g','x','x','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g',Tile(is_interactable= True, interact_text="You found me teeheehee"),'g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','x','x',Tile(is_ground=True, is_door=True, door_map= "TESTING_ZONE", door_coords=[7, 2]),'x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]
))

map_list.append(Map(name="TESTING_ZONE", grid=
[
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x',Tile(is_ground=True, is_door=True, door_map= "TEST_MAP", door_coords=[7,14]),'x','x','x','x','x','x','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g',Tile(is_interactable= True, interact_text="Second sign test!"),'g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]
))
