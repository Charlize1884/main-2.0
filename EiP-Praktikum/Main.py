import pygame
import pygame as pg
import os
from Player import Player
from World import World

def load_img(image_names: list) -> dict:
    images = {}
    try:
        for name in image_names:
            path = os.path.join('assets', name + '.png')
            image = pygame.image.load(path)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
            images[name] = image
    except FileNotFoundError:
        print(f'Image {path} not found')
        raise SystemExit
    return images

def main():
    #game setup
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
    image_names = ['Main_Background', 'Brickwall', 'Platform', 'Exit', 'Lava1', 'Spikedwall', 'Checkpoint', 'Ghost1']
    images_dict = load_img(image_names)
    background = pg.transform.scale(images_dict['Main_Background'], (1000, 800))

    #load map
    world_data =[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "g", 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 1],
    [1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 6, 6, 6, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 6, 0, 0, "g", 0, 0, 2, 2, 0, 0, "g", 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, "g", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, "g", 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 6, 2, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 6, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 0, "p", 0, 1, 1, 4, 4, 4, 4, 4, 1, 1, 6, 6, 1, 1, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    ]

    world = World()
    world.load_map(world_data, images_dict, 50)

    #load player from map
    row_count = 0
    for i in world_data:
        col_count = 0
        for j in i:
            if j == "p":
                player = Player(col_count*tile_size, row_count*tile_size, tile_size)
                break
            else:
                col_count += 1
        row_count += 1

    #MAIN LOOP
    run = True
    while run:
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE]:
            pg.quit()
        clock.tick(fps)

        #draw background
        screen.blit(background, (0, 0))

        #update enemy entities
        for enemy in world.enemy_list:
            enemy.update()

        #level scrolling

        #scroll down
        while player.rect.bottom > screen_height - 100:
            player.rect.y -=10
            player.respawnpoint[1] -=10
            for entity in world.tile_list:
                entity.rect.y -=10
            for enemy in world.enemy_list:
                enemy.rect.y -=10
            for block in world.fake_tile_list:
                block.rect.y -=10
        #scroll up
        while player.rect.top < screen_height / 3:
            player.rect.y +=10
            player.respawnpoint[1] +=10
            for entity in world.tile_list:
                entity.rect.y +=10
            for enemy in world.enemy_list:
                enemy.rect.y +=10
            for block in world.fake_tile_list:
                block.rect.y +=10
        #scroll left
        while player.rect.left > screen_width - screen_width / 2:
            player.rect.x -= 5
            player.respawnpoint[0] -= 5
            for entity in world.tile_list:
                entity.rect.x -= 5
            for enemy in world.enemy_list:
                enemy.rect.x -= 5
            for block in world.fake_tile_list:
                block.rect.x -= 5
        #scroll right
        while player.rect.right < screen_width / 2:
            player.rect.x += 5
            player.respawnpoint[0] += 5
            for entity in world.tile_list:
                entity.rect.x += 5
            for enemy in world.enemy_list:
                enemy.rect.x += 5
            for block in world.fake_tile_list:
                block.rect.x += 5

        #update player
        player.update(world, screen_height)

        #camera handling
        camera_offset_x = -max(world.tile_list[0].rect.left, 0)
        if camera_offset_x == 0:
            camera_offset_x= max(screen_width- world.tile_list[len(world_data[0])-1].rect.right, 0)

        camera_offset_y = -max(world.tile_list[0].rect.top, 0)
        if camera_offset_y == 0:
            camera_offset_y = max(screen_height- world.fake_tile_list[-1].rect.bottom, 0)
        world.draw(screen, camera_offset_x,camera_offset_y)
        world.draw_enemies(screen, camera_offset_x,camera_offset_y)
        player.draw(screen, camera_offset_x, camera_offset_y)

        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()