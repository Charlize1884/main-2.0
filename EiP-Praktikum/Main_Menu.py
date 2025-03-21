import pygame as pg
import sys
from button import Button

pg.init()

SCREEN = pg.display.set_mode((1200, 700))
pg.display.set_caption("Menu")

BACKGROUND = pg.image.load("assets/Background.png")
BACKGROUND = pg.transform.scale(BACKGROUND, (1200, 700))

def get_font(size):
    return pg.font.Font("font.ttf", size)


def play():
    pg.display.set_caption("Game")

    while True:

        PLAY_MOUSE_POS = pg.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the play screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center = (610, 300))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image = None, pos = (610, 500), text_input = "BACK", font = get_font(75), base_color = "White", hovering_color = "Gray")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()

def main_menu():
    pg.display.set_caption("Menu")

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center = (608, 200))

        PLAY_BUTTON = Button(image = pg.image.load("assets/Play_Rect.png"), pos = (608, 350), text_input ="PLAY", font = get_font(70), base_color ="Black", hovering_color ="Gray")
        QUIT_BUTTON = Button(image = None,pos = (608, 500), text_input = "QUIT", font = get_font(70),base_color = "Black", hovering_color = "Gray")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()





