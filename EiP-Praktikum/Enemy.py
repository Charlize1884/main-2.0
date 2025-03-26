import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, hitpoints, damage, speed, action_speed, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (tile_size - 5, tile_size - 5))
        self.rect = self.image.get_rect()
        self.hitpoints = hitpoints
        self.damage = damage
        self.speed = speed
        self.y_speed = 0
        self.x_speed = 0
        self.rect.x = x
        self.rect.y = y
        self.action_speed = action_speed

