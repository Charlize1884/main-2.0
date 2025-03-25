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
                    self.tile_list.append(Wall(col_count*tile_size, row_count*tile_size, tile_size))
                if tile == 9:
                    self.fake_tile_list.append(Wall(col_count * tile_size, row_count * tile_size, tile_size))
                elif tile == 2:
                    self.tile_list.append(Platform(col_count*tile_size, row_count*tile_size, tile_size))
                elif tile == 3:
                    self.tile_list.append(Exit(col_count*tile_size, row_count*tile_size, tile_size))
                elif tile == 4:
                    self.tile_list.append(Lava(col_count*tile_size, row_count*tile_size, tile_size))
                elif tile == "g":
                    self.enemy_list.append(Patroling_Ghost(col_count*tile_size, row_count * tile_size, tile_size))

                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile.image, tile.rect)
        for tile in self.fake_tile_list:
            screen.blit(tile.image, tile.rect)