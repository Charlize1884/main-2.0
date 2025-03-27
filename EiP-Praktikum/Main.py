import pygame
import os
from Player import Player
from World import World
from Levels import world_data


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
current_level = 0
def main(current_level):
    #game setup
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screen_width = 960
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Platformer")

    #define game variables
    tile_size = 50

    #load images
    world_image_names = ['Main_Background', 'Brickwall', 'Platform', 'Exit', 'Lava1', 'Spikedwall', 'Checkpoint', 'Ghost1']
    world_images_dict = load_img(world_image_names)
    player_image_names = ['NinjaWalk1', 'NinjaWalk2', 'NinjaWalk3', 'NinjaHurt']
    player_images_dict = load_img(player_image_names)
    background = pygame.transform.scale(world_images_dict['Main_Background'], (1000, 800))

    #load map
    while current_level < len(world_data):
        player = Player(0, 0, player_images_dict, tile_size)
        world = World()
        world.load_map(world_data[current_level], world_images_dict, 50, player)

        #MAIN LOOP
        run = True
        while run:
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pygame.quit()
                raise SystemExit
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
                camera_offset_x= max(screen_width- world.tile_list[len(world_data[current_level][0])-1].rect.right, 0)

            camera_offset_y = -max(world.tile_list[0].rect.top, 0)
            if camera_offset_y == 0:
                camera_offset_y = max(screen_height- world.fake_tile_list[-1].rect.bottom, 0)
            world.draw(screen, camera_offset_x,camera_offset_y)
            world.draw_enemies(screen, camera_offset_x,camera_offset_y)
            player.draw(screen, camera_offset_x, camera_offset_y)
            print(world.tile_list[-1].rect)

            pygame.display.update()
            if player.level > current_level:
                current_level += 1
                run = False

    pygame.quit()


if __name__ == "__main__":
    main(current_level)