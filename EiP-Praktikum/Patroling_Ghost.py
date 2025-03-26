import pygame
from Patroling_Enemy import Patroling_Enemy

class Patroling_Ghost(Patroling_Enemy):
    def __init__(self, x_coord, y_coord, tile_size):
        Patroling_Enemy.__init__(self, x_coord, y_coord,'assets/Ghost_1.png', 2, 1, 14/6, 0, tile_size, 1)
    def update(self):
            self.patrol(50)

