import pygame as pg

pg.init()

screen = pg.display.set_mode((1200, 700))
pg.display.set_caption('Dungeon')

background = pg.image.load('assets/Main_Background.png')
game_active = True
while game_active:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_active = False
            print("Game Over")

    screen.fill((0, 200, 0))

    background = pg.transform.scale(background, (1200, 700))
    screen.blit(background, (0, 0))
    pg.display.flip()


