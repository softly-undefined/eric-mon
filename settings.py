from enum import Enum

class FACING(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

GRID_SIZE = 50  # Size of each grid unit

#15 x 9 is the 
SCREEN_WIDTH = GRID_SIZE * 15
SCREEN_HEIGHT = GRID_SIZE * 15

FPS = 60