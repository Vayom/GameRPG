class StaticItem:
    def __init__(self, title, hp, attack, speed, crit_chance, crit_damage, avoid_chance):
        self.used = False
        self.title = title
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.avoid_chance = avoid_chance

