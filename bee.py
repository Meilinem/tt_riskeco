class   Bee:
    hp = 0
    damage = 0
    b_type = ""

    def     __init__(self, hp, damage, b_type):
        self.hp = hp
        self.damage = damage
        self.b_type = b_type

    def     hit(self):
        self.hp -= self.damage
        return self.hp
