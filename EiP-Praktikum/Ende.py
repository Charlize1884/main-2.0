import pygame

class Ende():
    def __init__(self, x, y, tile_size):
        ende_img = pygame.image.load("assets/Ninja_Walk1.png")
        self.image = pygame.transform.scale(ende_img, (tile_size - 5, tile_size - 5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Ende_Game(self):
        pygame.quit()