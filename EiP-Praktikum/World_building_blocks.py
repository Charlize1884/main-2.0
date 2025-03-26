import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y, image, tile_size)


class Platform(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y, image, tile_size)


class Exit(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y, image, tile_size)


class Lava(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y + 10, image, tile_size)
        self.damage = 6


class SpikedWall(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y, image, tile_size)
        self.damage = 6


class Checkpoint(Tile):
    def __init__(self, x, y, image, tile_size):
        Tile.__init__(self, x, y, image, tile_size)
