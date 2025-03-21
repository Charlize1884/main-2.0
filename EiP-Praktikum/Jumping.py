import pygame as pg
import sys

pg.init()

CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode((1200, 700))
pg.display.set_caption("Game")

X_POSITION, Y_POSITION = 400, 600

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 15
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pg.transform.scale(pg.image.load("assets/Ninja_Jump.png"), (100, 100))
JUMPING_SURFACE =pg.transform.scale(pg.image.load("assets/Ninja_Walk1.png"), (100, 100))
BACKGROUND = pg.image.load("assets/Main_Background.png")

player_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    SCREEN.fill((0, 200, 0))
    BACKGROUND = pg.transform.scale(BACKGROUND, (1200, 700))

    keys_pressed = pg.key.get_pressed()

    if keys_pressed[pg.K_SPACE]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))

    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
            player_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            SCREEN.blit(JUMPING_SURFACE, player_rect)
        else:
            player_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
            SCREEN.blit(STANDING_SURFACE, player_rect)


    pg.display.update()
    CLOCK.tick(60)
