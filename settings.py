from enum import Enum
import maps

class FACING(Enum): #note the checking of the array goes updown then leftright
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]

GRID_SIZE = 50  # Size of each grid unit



#15 x 9 is the pokemon ruby size
SCREEN_WIDTH = GRID_SIZE * 15
SCREEN_HEIGHT = GRID_SIZE * 9

FPS = 15

MOVEMENT_DELAY = 400