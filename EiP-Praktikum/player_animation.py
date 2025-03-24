from player import Player
import pygame
from pygame.locals import *

def update(self, world, screen, screen_height):
    key = pygame.key.get_pressed()
    keys_down = pygame.event.get(pygame.KEYDOWN)
    for k in keys_down:
        if k.type == pygame.KEYDOWN:
            if k.key == K_SPACE and self.jumps > 0:
                self.vel_y = -15
                self.jumps -= 1
    if key[pygame.K_LEFT]:
        self.counter += 1
        self.direction = -1
    if key[pygame.K_RIGHT]:
        self.counter += 1
        self.direction = 1
    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
        self.counter = 0
        self.index = 0
        self.image = self.images_right[self.index]

        # handle animation
        if self.counter > Player.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

