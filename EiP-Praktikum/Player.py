from pygame.locals import *
from World_building_blocks import *
from ultilities import *


class Player():
    def __init__(self, x, y, tile_size):

        #graphic
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.tile_size = tile_size
        for num in range(1, 4):
            img_right = pygame.image.load(f"assets/Ninja_Walk{num}.png")
            img_right = pygame.transform.scale(img_right, (self.tile_size-5 , self.tile_size-5 ))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]

        #position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.respawnpoint=[(self.rect.left), (self.rect.top)]
        self.width =  self.image.get_width()
        self.height = self.image.get_height()

        #movement
        self.vel_y = 0
        self.speed = 5
        self.dash = True
        self.can_dash = True
        self.time_since_dashed = 0
        self.can_move = True
        self.can_jump = True
        self.jumps = 0
        self.maxjumps = 2
        self.direction = 0
        self.horizontal_scroll_pos = x
        self.vertical_scroll_pos = y

        #enemy interaction
        self.hitpoints = 6
        self.hit = False
        self.time_since_last_hit = 0


    def update(self, world, screen_height):
        dx = 0
        dy = 0

        walk_cooldown = 8

        #get key presses
        key = pygame.key.get_pressed()
        pygame.event.clear()

        if key[pygame.K_LCTRL] and self.can_dash and self.dash:
            self.can_dash = False
            self.can_move = False
            self.dash = False

        if not self.can_dash:
            if self.time_since_dashed <= 6:
                if self.direction == 1:
                    dx = 30
                else:
                    dx = -30

            if self.time_since_dashed > 6:
                self.can_move = True
            if self.time_since_dashed > 24:
                self.can_dash = True
                self.time_since_dashed = 0
            self.time_since_dashed += 1
        if self.can_move:
            if key[pygame.K_LSHIFT]:
                self.speed = 7
            else:
                self.speed = 4
        if key[K_SPACE] and self.jumps > 0 and self.can_jump and self.can_move:
            self.vel_y = -15
            self.jumps -= 1
        if key[K_SPACE]:
            self.can_jump = False
        else:
            self.can_jump = True
        if key[pygame.K_a] and self.can_move:
            dx -= self.speed
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d] and self.can_move:
            dx += self.speed
            self.counter += 1
            self.direction = 1
        if key[pygame.K_d] == False and key[pygame.K_a] == False:
            self.counter = 0
            self.index = 0
            self.image = self.images_right[self.index]

        #handling animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        #add gravity
        if self.can_move:
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

        #check for collision
        for tile in world.tile_list:

            #check for collision with platform block
            if type(tile) == Wall or type(tile) == Platform:
                #check for collision in x direction
                if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    if center_distance(self.rect, tile.rect)[0][0]>0:
                        dx = tile.rect.right - self.rect.left
                    else:
                        dx = tile.rect.left - self.rect.right

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
                        self.dash = True
            elif type(tile)==Lava or type(tile)==SpikedWall:
                if tile.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                    self.hitpoints = 0
                    self.hit = True
            elif type(tile)==Checkpoint:
                if tile.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                     self.respawnpoint = [tile.rect.left, tile.rect.top]

            #check for collision with exit block
            elif type(tile)==Exit:
                if tile.rect.colliderect(self.rect) and key[K_w]:
                    pygame.quit()


        #animation for hurt ninja
        if self.hit:
            if self.hitpoints <= 0:
                self.rect.left, self.rect.top = self.respawnpoint[0], self.respawnpoint[1]
                self.hitpoints = 6
            elif self.time_since_last_hit < 20:
                self.image = pygame.transform.scale(pygame.image.load("assets/Ninja_Hurt.png"), (self.tile_size - 5, self.tile_size - 5))
            if self.time_since_last_hit == 45:
                self.hit = False
            self.time_since_last_hit += 1

        #check for collision with enemies
        else:
            self.time_since_last_hit = 0
            for hitbox in world.enemy_list:
                if pygame.Rect.colliderect(self.rect, hitbox.rect) and self.hit == False:
                    self.hitpoints -= hitbox.damage
                    self.hit = True

                    distance = center_distance(self.rect, hitbox.rect)
                    self.vel_x = distance[0][0]*5


        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        self.horizontal_scroll_pos += dx
        self.vertical_scroll_pos += dy
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def draw(self, screen, camera_offset_x, camera_offset_y):
        offset_rect = pygame.Rect(self.rect.x+camera_offset_x, self.rect.y+camera_offset_y, self.rect.width, self.rect.height)
        screen.blit(self.image, offset_rect)