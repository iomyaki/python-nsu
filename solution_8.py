from random import random


class Person:
    def __init__(self, name, hp, speed, damage, defense, agility, crit):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.defense = defense
        self.agility = agility
        self.crit = crit

    def receive_damage(self, damage):
        res_dmg = damage - self.defense
        if res_dmg > 0:
            self.hp -= res_dmg

    def critical(self):
        return random() <= self.crit

    def dodge(self):
        return random() <= self.agility


def battle(person_1, person_2):
    players = [person_1, person_2] if person_1.speed >= person_2.speed else [person_2, person_1]

    while players[0].hp > 0 and players[1].hp > 0:
        if players[1].dodge():
            #print(f'{players[1].name} dodged the attack\n')
            continue
        else:
            dmg = (players[0].damage * 2) if players[0].critical() else players[0].damage
            players[1].receive_damage(dmg)
            #print(f'{players[0].name} applied {dmg} damage')
            #print(f'{players[1].name} now has {players[1].hp} HP\n')

        if players[1].hp <= 0:
            #print(f'{players[0].name} has won')
            return players[0]

        players.reverse()


wins_player_1 = 0
wins_player_2 = 0
for _ in range(100):
    player_1 = Person('Uglúk', 10, 1, 2, 1, 0, 0.5)
    player_2 = Person('Eltariel', 10, 1, 2, 1, 0.5, 0.5)

    if battle(player_1, player_2).name == player_1.name:
        wins_player_1 += 1
    else:
        wins_player_2 += 1

leader = player_1.name if wins_player_1 >= wins_player_2 else player_2.name

print(f'{player_1.name} - побед {wins_player_1}')
print(f'{player_2.name} - побед {wins_player_2}\n')
print(f'Наибольшее количество побед у персонажа с именем {leader}')
