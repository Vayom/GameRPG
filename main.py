import characters
from random import choice
from random import random

# name, level, hp, max_hp, attack, protection, speed, crit_chance, crit_damage, avoid_chance,
#                 block_status
plr = characters.Player(name='Vayom', level=1, hp=100, max_hp=100, attack=10, protection=0, speed=10, crit_chance=10,
                        crit_damage=100, avoid_chance=0, block_status=False)
enemy = characters.EnemyCharacter(name='Вурдалак блять', level=1, hp=50, max_hp=50, attack=10, protection=0, speed=11,
                                  crit_chance=5, crit_damage=100, avoid_chance=0, block_status=False)
plr.start_fight(enemy)

arr = [1, 2, 3, 4]
print(choice(arr))
print(round(random(), 2))
