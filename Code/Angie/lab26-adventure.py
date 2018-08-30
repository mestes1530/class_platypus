import random
import time
import chalk
import pygame
# re-use previous labs (guess the number, rock-paper-scissors)

#function for audio
def audio(audio_file):
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound(audio_file)
    sounda.play()
    #time.sleep(3)
    #sounda.stop()
    return sounda
audio('audio/Cat-meow-3.wav')
class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Cat(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, chalk.blue('🐱'))
        self.name = []

    def __repr__(self):
        return self.name


class Special(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, chalk.yellow('🌿'))


class Food(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, chalk.green('🐟'))



class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👧')
        self.cats = []
        self.catnip = 0
        self.fish = 0

    def inventory(self):  # maintains a list of items
        print(', '.join(self.cats))
        print(', '.join(self.special))

    def check_inventory(self):
        return f'You currently have {self.fish} fish and a {self.special} in your inventory'

    def __str__(self):
        return f'cats: {len(self.cats)}, fish: {self.fish}, catnip: {self.catnip}'


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



board = Board(10, 10)
pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
cats = []
foods = []
specials = []

for i in range(10):
    ei, ej = board.random_location()
    cat = Cat(ei, ej)
    entities.append(cat)
    cats.append(cat)

for i in range(10):
    ei, ej = board.random_location()
    food = Food(ei, ej)
    entities.append(food)
    foods.append(food)

for i in range(2):
    ei, ej = board.random_location()
    special = Special(ei, ej)
    entities.append(special)
    specials.append(special)

# x = random.randint(1, 10)
print(chalk.red('''

   ____      _      ____      _ _           _             
  / ___|__ _| |_   / ___|___ | | | ___  ___| |_ ___  _ __ 
 | |   / _` | __| | |   / _ \| | |/ _ \/ __| __/ _ \| '__|
 | |__| (_| | |_  | |__| (_) | | |  __/ (__| || (_) | |    
  \____\__,_|\__|  \____\___/|_|_|\___|\___|\__\___/|_|   
                                                   _
             |\___/|                      \\
             )     (    |\_/|              ||
            =\     /=   )a a `,_.-""""-.  //
              )===(    =\Y_= /          \//
             /     \     `"`\       /    /
             |     |         |    \ |   /         
            /       \         \   /- \  \
            \       /         || |  // /`
  _/\_/\_/\_ /\_/\_/\_/\_/\_((_|\((_//\_/\_/\_/\_




'''))

time.sleep(2)

while True:
    board.print(entities)

    command = input('what is your command? make a move, check cats, or check inventory').lower()  # get the command from the user

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
    elif command in ['check cats', 'cats']:
        print(f'{player.cats} you have collected {len(player.cats)} cats.')
    elif command in ['check inventory', 'inventory']:
        print(player)

    for cat in cats:
        if cat.location_i == player.location_i and cat.location_j == player.location_j:
            print('you\'ve encountered a kitty!')
            action = input('what will you do? ')
            if action == 'collect':
                print('you\'ve captured a kitty')
                audio('audio/Cat-meow-3.wav')
                name = input('what will you name the kitty?')
                cat.name = name
                player.cats.append(cat)
                # put the kitty name in your inventory
                entities.remove(cat)
                cats.remove(cat)
            else:
                print('you hesitated and the kitty ran off')
                exit()

    for food in foods:
        if food.location_i == player.location_i and food.location_j == player.location_j:
            print('you\'ve encountered a fish')
            action = input('what will you do? ')
            if action == 'collect':
                player.fish += 1
                print('you\'ve collected some food')
                # put the food in your inventory
                entities.remove(food)
                foods.remove(food)
            else:
                print('you hesitated and another kitty stole the food')
                player.fish -= 1
                exit()

    for special in specials:
        if special.location_i == player.location_i and special.location_j == player.location_j:
            print('you\'ve found catnip!')
            action = input('what will you do? ')
            if action == 'collect':
                player.catnip += 1
                print('you\'ve collected some catnip')
                # put the food in your inventory
                entities.remove(special)
                specials.remove(special)
            else:
                print('you lost some catnip')
                player.catnip -= 1
                exit()

    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)


    # check if the cats list is empty, if so, tell the user won
    if len(cats) == 0:
        print(f'You collected all the cats! you won! Here are your cats {player.cats}')
        break
    else:
        print('You did not collect all the cats, you lose!')