import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Wall(Tile):
    def __init__(self, x, y, tile_size):
        Tile.__init__(self, x, y, "assets/brick_wall.png", tile_size)


class Platform(Tile):
    def __init__(self, x, y, tile_size):
        Tile.__init__(self, x, y, "assets/Jumping_Pad_4.png", tile_size)

class Exit(Tile):
    def __init__(self, x, y, tile_size):
        Tile.__init__(self, x, y, "assets/Exit.png", tile_size)

class Lava(Tile):
    def __init__(self, x, y, tile_size):
        Tile.__init__(self, x, y+10, "assets/Lava.png", tile_size)



