from tile import Tile, Sign, Door
import maps
import settings


# how to integrate npc's into this? must have their own codes (how to make them turn and stuff)
#
#
#
#
#


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
                elif col == 'g' or col=='': #basic ground tile
                    obj_map.grid[row_index][col_index] = Tile(is_ground=True)
            if isinstance(col, Tile):
                obj_map.grid[row_index][col_index] = col

    return obj_map #now has the same size array for the space but full of Tile objects

class Map:
    def __init__(self, name='', grid=None):
        self.name = name
        self.grid = grid

map_list.append(Map(name="UP_TOWN", grid=
[
['x', 'x', 'x', 'x', 'x', 'x', 'x'],
['x', 'x', 'g', Sign(text=" What's up this is the sign for the secret extra up room!"), 'g', 'x', 'x'],
['x', 'g', 'g', 'g', 'g', 'g', 'x'],
['x', 'g', 'g', 'g', 'g', 'g', 'x'],
['x', 'g', 'g', 'g', 'g', 'g', 'x'],
['x', 'x', 'g', 'g', 'g', 'x', 'x'],
['x', 'x', 'x', Door(travel_to="TEST_MAP", coords=[7, 1]), 'x', 'x', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x']
]
))

map_list.append(Map(name="TEST_MAP", grid=
[
['x','x','x','x','x','x','x', 'x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x', Door(travel_to="UP_TOWN", coords=[3, 5]),'x','x','x','x','x','x','x'],
['x',Sign(text="NEW THING NEW THING"),'g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g',Sign(text="test number 3"),'g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','x','g','x','g','g','g','g','g','x'],
['x','x','x','x','x','x','x','g','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','g','x','x','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g',Sign(text="You found me teeheehee"),'g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','g','g','g','g','g','x','x','x','x','x'],
['x','x','x','x','x','x','x',Door(travel_to= "TESTING_ZONE", coords=[4, 2]),'x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]
))

map_list.append(Map(name="TESTING_ZONE", grid=
[
['x','x','x','x','x','x','x','x','x'],
['x','x','x','x',Door(travel_to= "TEST_MAP", coords=[7,40]),'x','x','x','x'],
['x','x','x','x','g','x','x','x','x'],
['x','x','g','g','g','g','x','x','x'],
['x','x','x','g','g','g','x','x','x'],
['x','g','g','g','g','g','x','x','x'],
['x','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','g','x'],
['x','g','g','g','g','g','g','x','x'],
['x','x','x','g','g','g','g','g','x'],
['x','x','x','g','x','g','g','g','x'],
['x','x','x','x','x','x','x','x','x'],
]
))
