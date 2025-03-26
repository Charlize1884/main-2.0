from PatrolingEnemy import PatrolingEnemy

class PatrolingGhost(PatrolingEnemy):
    def __init__(self, x_coord, y_coord, tile_size):
        PatrolingEnemy.__init__(self, x_coord, y_coord, 'assets/Ghost_1.png', 2, 1, 14 / 6, 0, tile_size, 1)
    def update(self):
            self.patrol(200)

