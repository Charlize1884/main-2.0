import pygame
from World_building_blocks import *
from Patroling_Ghost import Patroling_Ghost

class World:
    def __init__(self):
        self.tile_list = []
        self.fake_tile_list = []
        self.enemy_list = []


    def load_map(self, data, tile_size):
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    object = Wall(col_count*tile_size, row_count*tile_size, tile_size)
                    self.tile_list.append(object)
                if tile == 9:
                    object = Wall(col_count * tile_size, row_count * tile_size, tile_size)
                    self.fake_tile_list.append(object)
                elif tile == 2:
                    object = Platform(col_count*tile_size, row_count*tile_size, tile_size)
                    self.tile_list.append(object)
                elif tile == 3:
                    object = Exit(col_count*tile_size, row_count*tile_size, tile_size)
                    self.tile_list.append(object)
                elif tile == 4:
                    object = Lava(col_count*tile_size, row_count*tile_size, tile_size)
                    self.enemy_list.append(object)
                elif tile == 5 or tile == "p":
                    object = Checkpoint(col_count * tile_size, row_count * tile_size, tile_size)
                    self.tile_list.append(object)
                elif tile == 6:
                    object = Spiked_Wall(col_count * tile_size, row_count * tile_size, tile_size)
                    self.enemy_list.append(object)
                elif tile == "g":
                    object = Patroling_Ghost(col_count*tile_size, row_count * tile_size, tile_size)
                    self.enemy_list.append(object)
                col_count += 1
            row_count += 1


    def draw(self, screen, camera_offset_x, camera_offset_y):
        for tile in self.tile_list:
            offset_rect = pygame.Rect(tile.rect.x + camera_offset_x, tile.rect.y+camera_offset_y, tile.rect.width, tile.rect.height)
            screen.blit(tile.image, offset_rect)

        for tile in self.fake_tile_list:
            offset_rect = pygame.Rect(tile.rect.x + camera_offset_x, tile.rect.y+camera_offset_y, tile.rect.width, tile.rect.height)
            screen.blit(tile.image, offset_rect)


    def draw_enemies(self, screen, camera_offset_x, camera_offset_y):
        for enemy in self.enemy_list:
            offset_rect = pygame.Rect(enemy.rect.x + camera_offset_x, enemy.rect.y+camera_offset_y, enemy.rect.width, enemy.rect.height)
            screen.blit(enemy.image, offset_rect)