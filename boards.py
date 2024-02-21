import settings, game
import pygame

class Level:
    def __init__(self) :
        # get the display surface
        # sprite setup
        self.create_map()
    def create_map(self) :
        for row in settings.WORLD_MAP:
            print(row)
    def run (self):
        pass
# update and draw the game