from random import randint, choice, random


class Character:
    '''
    Описание
        Класс персонажа. В нём описаны методы, присущие любому игровому персонажу.

    Методы:
        1) take_damage - получение урона персонажем
        2) set_block - установка статуса блокирования следующей атаки
        3) escape - попытка сбежать с поля боя
        4) attack_enemy - нанесение урона персонажем
        5) death - метод проверки на смерть
        6) start_fight - интерфейс начала боя между персонажами
        7) fight - основной метод проведения боя

    Параметры:
        1) name - имя персонажа
        2) level - уровень персонажа
        3) hp - текущие Health Point (очки здоровья)
        4) max_hp - максимальное кол-во Health Point
        5) attack - количество урона, наносимое персонажем
        6) protection - броня
        7) speed - скорость (нужна для определения стороны для первого удара)
        8) crit_chance - шанс нанести крит. урон (в процентах от 0 до 100)
        9) crit_damage - урон, наносимый при срабатывании крита (в процентах от базовой атаки)
        10) avoid_chance - шанс парировать атаку соперника (в процентах)
        11) block_status - статус блокирования атаки
    '''

    def __init__(self, name, level, hp, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
                 block_status):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.protection = protection
        self.speed = speed
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.avoid_chance = avoid_chance
        self.block_status = block_status

    # Получение урона
    def take_damage(self, damage):
        self.hp -= damage - self.protection

    # Установка статуса блокирования
    def set_block(self):
        self.block_status = True
        print(f'{self.name} ставит блок')

    # Функция побега с поля боя
    def escape(self, enemy):
        diff_levels = enemy.level - self.level
        if diff_levels <= 0:
            escape_chance = 0.3
        elif diff_levels < 5:
            escape_chance = 0.1
        else:
            escape_chance = 0.05
        escaping = True if round(random(), 2) <= escape_chance else False
        if escaping:
            print('Получилось сбежать')
        else:
            print('Побег не удался')
        return escaping

    # Нанесение урона
    def attack_enemy(self, enemy):
        parrying_chance = 0.5 if enemy.block_status else 0
        parrying_chance = 0.5 + (0.5 * enemy.avoid_chance / 100) if parrying_chance == 0.5 else enemy.avoid_chance / 100
        rand_attack = round(random(), 2)
        print(f'Шанс парирования у {enemy.name} = {parrying_chance}')
        attacking = True if rand_attack > parrying_chance else False
        if attacking:
            enemy.take_damage(self.attack)

            print(f'{self.name} нанёс {self.attack - enemy.protection} по {enemy.name}')
        else:
            print(f'{enemy.name} парировал атаку')

    # Проверка на смерть
    def death(self):
        return self.hp <= 0

    def start_fight(self, enemy_char):
        '''
        Описание
            Метод начала и проведения боя, с информированием о конечном результате

        Параметры:
            enemy_char - объект персонажа, с которым будет проходить бой

        '''
        print('Бой начался')
        # Основной метод проведения боя вызывается от игрока, если у него не меньше очков, чем у врага
        if self.speed >= enemy_char.speed:
            print('Вы ходите первыми')
            first_move = True
        else:
            print(f'Сначала ходит {enemy_char.name}')
            first_move = False
        result = self.fight(enemy_char, first_move)
        if result == 'Win':
            print('Победа')
            enemy_char.give_drop(self)
        elif result == 'Lose':
            print('Умер лох(')
            exit()
        # Проверка на конечный результат

    def fight(self, enemy_char, player_first):
        '''
        Описание
            Основной метод боя, игрок способен выбрать действие, противник - нет.
            Первый ход определяет переменная player_first
            Бой длится до тех пор, пока игрок не сбежит или какая-то из сторон не погибнет
        '''
        actions = ['Атаковать', 'Защищаться']
        first_move_end = False
        result = 0
        while self.hp > 0 and enemy_char.hp > 0:
            if player_first or not first_move_end:
                choice_action = int(input('Выберите действие\n1) Атаковать\n2) Защититься\n3) Сбежать\n'))
                if choice_action == 1:
                    self.attack_enemy(enemy_char)
                elif choice_action == 2:
                    self.set_block()
                elif choice_action == 3:
                    escaping = self.escape(enemy_char)
                    if escaping:
                        return 'escaped'
            enemy_action = choice(actions)
            enemy_char.block_status = False
            if enemy_action == 'Атаковать':
                enemy_char.attack_enemy(self)
            else:
                enemy_char.set_block()
            self.block_status = False
            first_move_end = True
        result = 'Win' if self.hp > 0 else 'Lose'
        return result


class Player(Character):
    '''
    Описание
        Класс основного действующего лица.

    Методы:
        1) show_inventory - показ всех вещей в инвентаре
    '''

    def __init__(self, name, hp, level, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
                 block_status):
        super().__init__(name, hp, level, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
                         block_status)
        self.inventory = []
        self.static_items = {'first_weapon': None,
                             'helmet': None,
                             'bib': None,
                             'pants': None,
                             'boots': None,
                             'ring_1': None,
                             'ring_2': None,
                             'accessories': None,
                             'pet': None}

    def show_inventory(self):
        for item in self.inventory:
            print(item)

    def put_on(self, item):
        pass


class EnemyCharacter(Character):
    '''
    Описание
        Класс враждебных существ, имеют инвентарь дропающихся предметов

    Методы:
        1) give_drop - метод, который случайным образом выдаёт или не выдает предметы игроку
    '''

    def __init__(self, name, level, hp, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
                 block_status):
        super().__init__(name, level, hp, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
                         block_status)
        self.drop = {'Меч': 0.5, 'Золотой шлем': 0.2}

    def give_drop(self, player):
        for item, chance in self.drop.items():
            get_chance = round(random(), 2)
            if get_chance <= chance:
                player.inventory.append(item)
                print(f'Добавлен предмет {item}')
