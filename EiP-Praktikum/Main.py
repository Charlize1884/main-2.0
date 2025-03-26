import pygame
import pygame as pg
from pygame.locals import *
from Player import Player
from World import World
from Patroling_Ghost import Patroling_Ghost
from Button import Button

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
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 , 1],
[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, "g", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "g", 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9],
[1, 0, "p", 0, 0, 1, 1, 9, 9, 9, 9, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]
row_count = 0
world = World(world_data, tile_size)
for i in world_data:
    col_count = 0
    for j in i:
        if j == "p":
            player = Player(col_count*tile_size, row_count*tile_size, tile_size)
        col_count += 1
    row_count += 1

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
    while player.rect.bottom > screen_height - 100:
        player.rect.y -=10
        player.respawnpoint[1] -=10
        for entity in world.tile_list:
            entity.rect.y -=10
        for enemy in world.enemy_list:
            enemy.rect.y -=10
        for block in world.fake_tile_list:
            block.rect.y -=10
    while player.rect.bottom < screen_height / 3:
        player.rect.y +=10
        player.respawnpoint[1] +=10
        for entity in world.tile_list:
            entity.rect.y +=10
        for enemy in world.enemy_list:
            enemy.rect.y +=10
        for block in world.fake_tile_list:
            block.rect.y +=10
    while player.rect.left > screen_width - screen_width / 2:
        player.rect.x -= 5
        player.respawnpoint[0] -= 5
        for entity in world.tile_list:
            entity.rect.x -= 5
        for enemy in world.enemy_list:
            enemy.rect.x -= 5
        for block in world.fake_tile_list:
            block.rect.x -= 5
    while player.rect.right < screen_width / 2:
        player.rect.x += 5
        player.respawnpoint[0] += 5
        for entity in world.tile_list:
            entity.rect.x += 5
        for enemy in world.enemy_list:
            enemy.rect.x += 5
        for block in world.fake_tile_list:
            block.rect.x += 5
    player.update(world, screen_height)
    #graphics

    world.draw(screen)
    world.draw_enemys(screen)
    player.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()

pg.quit()

