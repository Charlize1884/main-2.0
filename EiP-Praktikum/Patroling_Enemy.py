from Enemy import Enemy
class Patroling_Enemy(Enemy):
    def __init__(self, x, y, image, hitpoints, damage, speed, action_speed, tile_size ,move_direction):
        Enemy.__init__(self, x, y, image, hitpoints, damage, speed, action_speed, tile_size)
        self.move_counter = 0
        self.move_direction = move_direction
    def patrol(self, range):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter>range:
            self.move_direction*=-1
            self.move_counter*=-1