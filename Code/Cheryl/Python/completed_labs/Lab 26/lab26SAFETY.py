#ST audio files from http://www.trekcore.com/audio/
#extra emojis ☄️

import os
import random

from termcolor import colored
import time

from colorama import Fore, Back, Style
import pygame
import time


def audio(audio_file):
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound(audio_file)
    sounda.play()
    time.sleep(3)


audio("st_audio/tos_bridge_1_activate.wav")


def end_credits():
    os.system('afplay st_audio/credits.wav &')


def style_files(path):
    with open(path, 'r') as f:
        # print(Style.DIM)
        print(Fore.YELLOW + Back.LIGHTBLACK_EX)
        return f.read()


print(style_files('title.txt'))
print(Style.RESET_ALL)
print(Back.LIGHTBLACK_EX)

#ending for roms vs feds
def romulan_vs_federation():
    end_credits()
    print(style_files('romulan.txt'))
    print('\tYou have been captured by the Romulans.')
    time.sleep(2)
    print('\n\tYou hold out hope and are eventually rescued')
    time.sleep(2)
    print('\n\tby Spock and his Romulan friends who are')
    time.sleep(2)
    print('\n\tattempting to reform the Romulan government.')


#Choose your race: Klingon or Federation
user_race = input('Choose your race: Klingon or Federation. >   ').upper()
if user_race == 'KLINGON':
    print(style_files('klingon.txt') + '\n\n\tYou chose to be a Klingon! \n\n')
else:
    print(style_files('federation.txt') + '\n\n\tYou chose to be a member of the Federation! \n\n')

time.sleep(3)

#Choose your enemy: Romulan or Borg
user_enemy = input('\nChoose your enemy: Romulan or Borg. >   \n\n').upper()

if user_enemy == 'BORG':
    print(style_files('borg.txt') + '\n\n\tYou chose to fight the Borg! \n\n')
else:
    print(style_files('romulan.txt') + '\n\n\tYou chose to fight the Romulans! \n\n')

time.sleep(2)

# #intro to game play
# print('\tTo play \'Space Trek\', just type:\n\t \'U\' for up, \'D\' for down, \'L\' for left, and \'R\' for right.\n\t To quit, type \'done.\'')
# time.sleep(5)
# print('\n\tThe stars will give you 5 points and help reinforce your shields.\n\tEach enemy that you fight can take away, or give you, 5 points. ')
# time.sleep(5)
# print(f'\n\tHave fun fighting the {user_enemy}!')
# time.sleep(5)

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        if user_enemy == "BORG":
            super().__init__(location_i, location_j, '🕋') #borg

        else:
            super().__init__(location_i, location_j, '👿') #romulan



class Player(Entity):
    def __init__(self, location_i, location_j):
        if user_race == "KLINGON":
            super().__init__(location_i, location_j, '👹') #klingon
        else:
            super().__init__(location_i, location_j, '🖖') #federation


class Shield(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🌟') #shield
#
#
# class Empty_Space(Entity):
#     def __init__(self, location_i, location_j):
#         super().__init__(location_i, location_j, '🌟') #empty space

print(Fore.BLACK + Back.CYAN)
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    # Returns a random location on the board
    def random_location_safe(self, entities):
        while True:
            location_i = random.randint(0, self.width - 1)
            location_j = random.randint(0, self.height - 1)
            for entity in entities:
                if entity.location_i == location_i and entity.location_j == location_j:
                    break
            else:
                break
        return location_i, location_j

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


print(Fore.BLACK + Back.CYAN)
board = Board(10, 10)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
# empty_spaces = []
enemies = []
shields = []

for i in range(10):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)

for i in range(3):
    ei, ej = board.random_location()
    shield = Shield(ei, ej)
    entities.append(shield)
    shields.append(shield)

# for i in range(10):
#     ei, ej = board.random_location()
#     empty_space = Empty_Space(ei, ej)
#     entities.append(empty_space)
#     empty_spaces.append(empty_space)

#sets points for game
points = 0
new_points = points
enemy_count = 0


while True:

    board.print(entities)

    command = input('What is your command? ')  # get the command from the user

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

    for shield in shields:
        if shield.location_i == player.location_i and shield.location_j == player.location_j:
            print('you\'re shields are at full power.')
            time.sleep(2)
            new_points += 5
            # print(shield_points)
            entities.remove(shield)
            shields.remove(shield)
            break
            time.sleep(3)


    # for empty_space in empty_spaces:
    #     if empty_space.location_i == player.location_i and empty_space.location_j == player.location_j:
    #         print('.')
    #         #
    #         # entities.remove(empty_space)
    #         # shields.remove(shield)
    #         break
    #         time.sleep(3)


    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            proximity_fire_audio = ["st_audio/phasersready.wav", 'st_audio/tactalertvesselapproach.wav']
            random_proximity_fire_audio = random.choice(proximity_fire_audio)
            audio(random_proximity_fire_audio)
            if user_enemy == 'BORG':
                print('You\'ve encountered a Borg cube.')
                action = input('Will you fire on it, or attempt to reason with them? ')
            else:
                print('You\'ve encountered a Romulan ship.')
                action = input('Will you fire on it, or attempt to reason with them? ')

            if action == 'fire':
                enemy_count += 1
                #adds random weapon sounds on fire
                fire_audio = ["st_audio/tng_weapons.wav", "st_audio/tos_photon_torpedo.wav", "st_audio/tng_torpedo.wav", "st_audio/tng_torpedo2.wav", "st_audio/tng_torpedo3.wav"]
                random_fire_audio = random.choice(fire_audio)
                audio(random_fire_audio)
                # print(enemy_count)
                if enemy_count == 10:
                    print('You\'ve won the game! ')
                    time.sleep(2)
                    if user_race == 'KLINGON':
                        audio('st_audio/largeexplosion.wav')
                        audio('st_audio/largeexplosion.wav')
                        time.sleep(0.5)
                        end_credits()
                        print(style_files('klingon_ship.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_two.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_three.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_four.txt'))

                        exit()
                    else:
                        time.sleep(0.5)
                        audio('st_audio/livelong.wav')
                        time.sleep(0.5)
                        end_credits()
                        print(style_files('federation_ship.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_two.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_three.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_four.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_five.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_six.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_seven.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_eight.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_nine.txt'))
                        time.sleep(0.25)
                        print(f"\n\n\n\n{style_files('federation_ship_ten.txt')}")

                        exit()

                #adds points or deducts random points based on who wins the attack
                win_lose = 'LOSE'
                # win_lose = ['WIN', 'LOSE']
                # win_lose = random.choice(win_lose)
                if win_lose == 'LOSE':
                    print('You\'ve lost the fight. ')
                    new_points -= 5
                    print(f'You now have: {new_points} points')
                    if new_points == 10:
                        audio('st_audio/primaryshieldsfailing.wav')
                    elif new_points == 5:
                        audio('st_audio/lifesupportfailureabandon.wav')
                    if new_points <= 0:
                    # IF YOU LOSE
                        audio('st_audio/largeexplosion.wav')
                        if user_enemy == "BORG":
                            print('You have been assimilated.')
                            time.sleep(3)
                            end_credits()
                            print(style_files('borg.txt') + '\t\tYou are now Borg...')

                        else:
                            if user_race == 'KLINGON':
                                time.sleep(1)
                                end_credits()
                                print(style_files(
                                    'romulan.txt') + '\t\tYou have been put in a Romulan Prison Camp where you will die a slow and dishonorable death.')

                            else:

                                print(romulan_vs_federation())
                                # end_credits()
                        # end_credits(audio)
                        exit()

                else:
                    print('you\'ve destroyed their ship!')
                    new_points += 5
                    print(f'You now have: {new_points} points')

                time.sleep(1.5)
                entities.remove(enemy)
                enemies.remove(enemy)
                break

            # elif enemy_count == 0:
            #     print('WORKING')
            else:
                print('You misfired and your ship has been destroyed.')
                time.sleep(3)
                if user_enemy == "BORG":
                    print('You have been assimilated.')
                    time.sleep(3)
                    end_credits()
                    print(style_files('borg.txt') + '\t\tYou are now Borg...')

                else:
                    if user_race == 'KLINGON':
                        time.sleep(1)
                        end_credits()
                        print(style_files(
                            'romulan.txt') + '\t\tYou have been put in a Romulan Prison Camp where you will die a slow and dishonorable death.')
                    else:
                        print(romulan_vs_federation())
                        # end_credits()
                # end_credits()
                exit()
