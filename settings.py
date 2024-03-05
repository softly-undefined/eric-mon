from enum import Enum

#
# Defines a whole punch of stuff
#
# 
#

class FACING(Enum): #note the checking of the array goes updown then leftright
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]

class MOVEMENT(Enum): #note the checking of the array goes updown then leftright
    WALK = 2
    RUN = 5
    BIKE = 10
    
GRID_SIZE = 70  # Size of each grid unit


#15 x 9 is the pokemon generation 3 size
SCREEN_WIDTH = GRID_SIZE * 15
SCREEN_HEIGHT = GRID_SIZE * 9
SCREEN_CENTER = [SCREEN_WIDTH // 2 - GRID_SIZE // 2, SCREEN_HEIGHT // 2 - GRID_SIZE // 2]



FPS = 60

MOVEMENT_DELAY = 400