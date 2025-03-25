import pygame
import pygame as pg
from pygame.locals import *
from player import Player
from world import World
from Patroling_Ghost import Patroling_Ghost
from button import Button

pg.init()

clock = pg.time.Clock()
fps = 60
screen_width = 960
screen_height = 640

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Platformer")

#define game variables
tile_size = 50

#load images
background = pg.image.load("assets/Main_Background 3.png")
background = pg.transform.scale(background, (1000, 800))

world_data =[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, "g", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9],
[1, 0, "p", 0, 0, 1, 1, 9, 9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]
row_count = 0
for i in world_data:
    col_count = 0
    for j in i:
        if j == "p":
              player = Player(col_count*tile_size, row_count*tile_size, tile_size)
        col_count += 1
    row_count += 1
world = World(world_data, tile_size)
run = True
while run:
    key = pg.key.get_pressed()
    if key[pg.K_ESCAPE]:
        pg.quit()
    clock.tick(fps)

    screen.blit(background, (0, 0))


    for Enemy in world.enemy_list:
        Enemy.update()

    #Level scrolling
    if player.rect.bottom > screen_height - 100:
        player.rect.y -= 15
        for entity in world.tile_list:
            entity.rect.y -= 15
        for enemy in world.enemy_list:
            enemy.rect.y -= 15
        for block in world.fake_tile_list:
            block.rect.y -= 15
    if player.rect.bottom < screen_height / 3:
        player.rect.y += 15
        for entity in world.tile_list:
            entity.rect.y += 15
        for enemy in world.enemy_list:
            enemy.rect.y += 15
        for block in world.fake_tile_list:
            block.rect.y += 15
    if player.rect.left > screen_width - screen_width / 2:
        player.rect.x -= 5
        for entity in world.tile_list:
            entity.rect.x -= 5
        for enemy in world.enemy_list:
            enemy.rect.x -= 5
        for block in world.fake_tile_list:
            block.rect.x -= 5
    if player.rect.right < screen_width / 2:
        player.rect.x += 5
        for entity in world.tile_list:
            entity.rect.x += 5
        for enemy in world.enemy_list:
            enemy.rect.x += 5
        for block in world.fake_tile_list:
            block.rect.x += 5
    player.update(world, screen_height)
    #graphics

    world.draw(screen)
    player.draw(screen)
    world.draw_enemys(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()

pg.quit()

