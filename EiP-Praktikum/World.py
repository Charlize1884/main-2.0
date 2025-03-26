import pygame
from World_building_blocks import *
from Patroling_Ghost import Patroling_Ghost

class World():
    def __init__(self,data, tile_size):
        self.tile_list = []
        self.fake_tile_list = []
        self.enemy_list = []


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
                elif tile == "g":
                    object = Patroling_Ghost(col_count*tile_size, row_count * tile_size, tile_size)
                    self.enemy_list.append(object)

                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile.image, tile.rect)
        for tile in self.fake_tile_list:
            screen.blit(tile.image, tile.rect)
    def draw_enemys(self, screen):
        for enemy in self.enemy_list:
            screen.blit(enemy.image, enemy.rect)