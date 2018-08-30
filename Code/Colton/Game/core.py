import random
import time

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '😈')
        self.health = 1
        self.strength = 1


class Big_Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👾')
        self.health = 2
        self.strength = 2


class Boss(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👺')
        self.health = 5
        self.strength = 3


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '😎')
        self.health = 20
        self.strength = 1


class Armor(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🛡️')
        self.health = 5


class Sword(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🗡️')
        self.strength = 2


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()


def boss_fight():
    boss = Boss(bi, bj)
    bosses = [boss]
    entities = [player, armor, boss]
    print(end_fight)
    time.sleep(5)
    print('Once you start this fight you wont be able to flee!')
    time.sleep(2)
    while True:

        board.print(entities)
        print(f' you have {player.health} health left and you are currently at {player.strength} strength.')

        command = input(f'{name}, what is your command? ')  # get the command from the user

        # movement controls
        if command == 'done':
            break  # exit the game
        elif command in ['l', 'left', 'w', 'west']:
            player.location_j -= 1  # move left
        elif command in ['r', 'right', 'e', 'east']:
            player.location_j += 1  # move right
        elif command in ['u', 'up', 'n', 'north']:
            player.location_i -= 1  # move up
        elif command in ['d', 'down', 's', 'south']:
            player.location_i += 1  # move down
        for boss in bosses:
            if boss.location_i == player.location_i and boss.location_j == player.location_j:
                while True:
                    print('you\'ve encountered the ogre!')
                    action = input('what will you do? ')
                    if action == 'attack':
                        roll = random.randint(0, 1)
                        if roll == 0 and player.strength >= boss.health:
                            print('You killed them!')
                            time.sleep(2)
                            print(win2)
                            time.sleep(2)
                            print(win)
                            entities.remove(boss)
                            bosses.remove(boss)
                            exit()
                        elif roll == 0 and player.strength < boss.health:
                            player.health -= boss.strength
                            boss.health -= player.strength
                            print(f'You hit him but his hide is too tough and he hit you. He has {boss.health} health left.')
                        elif roll == 1 and player.health > 0 and boss.strength < player.health:
                            player.health -= boss.strength
                            print(f'You missed and he got in a counter attack.')
                        else:
                            print(death)
                            print(f'thanks for trying {name} but your dead.')
                            exit()


board = Board(15, 15)
si, sj = board.random_location()
sword = Sword(si, sj)
ai, aj = board.random_location()
armor = Armor(ai, aj)
pi, pj = board.random_location()
player = Player(pi, pj)
entities = [player, sword, armor]
enemies = []
items = [sword, armor]


for i in range(0):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
for i in range(1):
    bi, bj = board.random_location()
    benemy = Big_Enemy(bi, bj)
    entities.append(benemy)
    enemies.append(benemy)
with open('welcome.txt', 'r') as f:
    welcome = f.read()
with open('death.txt', 'r') as f:
    death = f.read()
with open('end_fight.txt', 'r') as f:
    end_fight = f.read()
with open('win.txt', 'r') as f:
    win = f.read()
    with open('win2.txt', 'r') as f:
        win2 = f.read()
# instructions
print("Move: L(left), R(right), U(up), D(down) Encounter: Attack, Flee")
print(welcome)
print('We all live in this cave. But some bad guys have tried to take it over.')
name = input(f" Thanks for agreeing to kill them all, but first what should I call you? ")
time.sleep(1)
print(f'Nice to meet you {name}')
time.sleep(1)
print('What do you mean you didn\'t bring armor? maybe you can find some in the cave.')
time.sleep(3)


while True:

    board.print(entities)

    print(f' you have {player.health} health left and you are currently at {player.strength} strength.')

    command = input(f'{name}, what is your command? ')  # get the command from the user

# movement controls
    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down
# encounters

    if armor in entities and armor.location_i == player.location_i and armor.location_j == player.location_j:
        player.health += armor.health
        items.remove(armor)
        entities.remove(armor)
        print('You found some armor. Your health went up!')

    if sword in entities and sword.location_i == player.location_i and sword.location_j == player.location_j:
        items.remove(sword)
        entities.remove(sword)
        player.strength += sword.strength
        print('You found a sword. Your strength went up!')

    for enemy in enemies:
            if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
                print('you\'ve encountered an enemy!')
                action = input('what will you do? ')
                while True:
                    if action == 'attack':
                        if random.randint(0, 1) == 0 and player.strength >= enemy.health:
                            print('You killed them!')
                            entities.remove(enemy)
                            enemies.remove(enemy)
                            break
                        elif player.health > 0:
                            player.health -= enemy.strength
                            enemy.health -= player.strength
                            print('They got you.')
                            if player.health > 0:
                                fight = input(f'You have {player.health} left. Attack or flee?')
                                if fight == 'attack':
                                    if random.randint(0, 1) == 0 and player.strength >= enemy.health:
                                        entities.remove(enemy)
                                        enemies.remove(enemy)
                                        print('You killed them!')
                                        break
                                else:
                                    player.health -= 1
                                    print(f'you ran but they got a swipe on you {player.health} left.')
                                    break
                        else:
                            print(death)
                            print(f'thanks for trying {name} but your dead.')
                            exit()
                    else:
                        player.health -= 1
                        print(f'you ran but they got a swipe on you {player.health} left.')
                        break

    if not enemies:
        time.sleep(2)
        break
# move enemy on board
#     for enemy in enemies:
#         if random.randint(0, 1) == 0:
#             enemy.location_i += random.randint(-1, 1)
#         else:
#             enemy.location_j += random.randint(-1, 1)
boss_fight()

