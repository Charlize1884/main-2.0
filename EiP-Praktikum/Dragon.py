class Enemies:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount

class FlyingEnemies(Enemies):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)



dragon = Enemies(1, 1, 10)