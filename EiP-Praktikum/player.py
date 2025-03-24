import pygame
from World_building_blocks import *
from pygame.locals import *

class Player():
    def __init__(self, x, y, tile_size):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img_right = pygame.image.load(f"assets/Ninja_Walk{num}.png")
            img_right = pygame.transform.scale(img_right, (tile_size -5, tile_size -5))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width =  self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumps = 0
        self.maxjumps = 1
        self.direction = 0

    def update(self, world, screen, screen_height):
        dx = 0
        dy = 0
        walk_cooldown = 8

        #get key presses
        key = pygame.key.get_pressed()
        keys_down = pygame.event.get(pygame.KEYDOWN)
        for k in keys_down:
            if k.type == pygame.KEYDOWN:
                if k.key == K_SPACE and self.jumps > 0:
                    self.vel_y = -15
                    self.jumps -= 1
        if key[pygame.K_a]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            self.image = self.images_right[self.index]

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collision
        for tile in world.tile_list:

            if type(tile)==Wall or type(tile)==Platform:
                if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # check for collision in y direction
                if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile.rect.bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile.rect.top - self.rect.bottom
                        self.vel_y = 0
                        self.jumps = self.maxjumps

            elif type(tile)==Exit:
                if tile.rect.colliderect(self.rect) and key[K_w]:
                    pygame.quit()
        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        #draw player onto screen
        screen.blit(self.image, self.rect)