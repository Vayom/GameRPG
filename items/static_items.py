class StaticItem:
    '''
        Описание
            Класс статических предметов, которые игрок может надеть
        Параметры:
            1) title - название предмета
            2) hp - Health Point (очки здоровья)
            3) attack - количество урона, наносимое персонажем
            4) speed - скорость (нужна для определения стороны для первого удара)
            5) crit_chance - шанс нанести крит. урон (в процентах от 0 до 100)
            6) crit_damage - урон, наносимый при срабатывании крита (в процентах от базовой атаки)
            7) avoid_chance - шанс парировать атаку соперника (в процентах)
        '''

    def __init__(self, title, hp, attack, speed, crit_chance, crit_damage, avoid_chance):
        self.used = False
        self.title = title
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.avoid_chance = avoid_chance
