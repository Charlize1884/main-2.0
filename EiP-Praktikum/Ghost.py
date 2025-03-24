import pygame

from Enemy import Enemy

class Ghost(Enemy):
    def __init__(self, x_coord, y_coord, tile_size):
        Enemy.__init__(self, x_coord, y_coord,'assets/Ghost_1.png', 2, 1, 14/6, 0, tile_size, 1)

    def update(self, screen):
            self.patrol()
            screen.blit(self.image, self.rect)
import pygame


from Enemy import Enemy

class Ghost(Enemy):
    def __init__(self, x_coord, y_coord, tile_size):
        Enemy.__init__(self, x_coord, y_coord,'assets/Ghost_1.png', 2, 1, 14/6, 0, tile_size, 1)

    def update(self, screen):
            self.patrol()
            screen.blit(self.image, self.rect)
