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

def main_menu():
    pg.display.set_caption("Menu")

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pg.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Game Over", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center = (608, 200))

        RETRY_BUTTON = Button(image = pg.image.load("assets/Retry_Rect.png"), pos = (608, 350), text_input ="RETRY", font = get_font(70), base_color ="Black", hovering_color ="Gray")
        QUIT_BUTTON = Button(image = pg.image.load("assets/Quit_Rect.png"),pos = (608, 500), text_input = "QUIT", font = get_font(70),base_color = "Black", hovering_color = "Gray")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [RETRY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if RETRY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    retry()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()

main_menu()





