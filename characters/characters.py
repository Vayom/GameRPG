from random import randint


class Character:
    '''
    Описание
        Класс персонажа. В нём описаны методы, присущие любому игровому персонажу.

    Методы:
        1) take_damage - получение урона персонажем
        2) attack_enemy - нанесение урона персонажем
        3) death - метод проверки на смерть
        4) start_fight - интерфейс начала боя между персонажами
        5) fight - основной метод проведения боя

    Параметры:
        1) name - имя персонажа
        2) hp - Health Point (очки здоровья)
        3) attack - количество урона, наносимое персонажем
    '''

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    # Получение урона
    def take_damage(self, damage):
        self.hp -= damage

    # Нанесение урона
    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)

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
        rand_num_player = randint(1, 10)
        rand_num_enemy = randint(1, 10)
        print(f'Ваше число - {rand_num_player}\nЧисло врага - {rand_num_enemy}')
        # Основной метод проведения боя вызывается от игрока, если у него не меньше очков, чем у врага
        if rand_num_player >= rand_num_enemy:
            print('Вы ходите первыми')
            self.fight(enemy_char)
        else:
            print('Сначала бьёт враг')
            enemy_char.fight(self)
        # Проверка на конечный результат
        if not self.death():
            print('Победа!')
        else:
            print('Умер(')

    def fight(self, enemy_char):
        while self.hp > 0 and enemy_char.hp > 0:
            enemy_char.take_damage(self.attack)
            print(f'{self.name} наносит {self.attack} урона по {enemy_char.name}')
            if enemy_char.death():
                break
            self.take_damage(enemy_char.attack)
            print(f'{enemy_char.name} наносит {enemy_char.attack} урона по {self.name}')
            if self.death():
                break


class Player(Character):
    '''
    Описание
        Класс основного действующего лица.

    Методы:
        1) show_inventory - показ всех вещей в инвентаре
    '''
    def __init__(self, name):
        super().__init__(name, attack=10, hp=100)
        self.inventory = []

    def show_inventory(self):
        for item in self.inventory:
            print(item)


class EnemyCharacter(Character):
    '''
    Описание
        Класс враждебных существ, имеют инвентарь дропающихся предметов

    Методы:
        1) give_drop - метод, который случайным образом выдаёт или не выдает предметы игроку
    '''
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        self.drop = {'Меч': 50, 'Золотой шлем': 20}

    def give_drop(self, player):
        for item, chance in self.drop.items():
            get_chance = randint(1, 101)
            if get_chance <= chance:
                player.inventory.append(item)
                print(f'Добавлен предмет {item}')
