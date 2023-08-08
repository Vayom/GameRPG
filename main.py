import characters

plr = characters.Player('Vayom')
enemy = characters.EnemyCharacter('Huylo', attack=5, hp=500)
plr.start_fight(enemy)

print(enemy.drop)
enemy.give_drop(plr)
