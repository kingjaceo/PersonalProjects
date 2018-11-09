# sticks_game.py
# allows the user to play a simple game against a human opponent, a random ai, or a trained ai
# the rules are simple: players take turns taking between 1 and 3 sticks from the pile; whomever
# takes the last stick loses

# if the user wants to play against a trained ai, the program teaches an ai the optimal strategy
# using 200,000 games
import time
import random


def human_vs_human(n):
    player_one = 0
    player_two = 0
    while n > 0:
        print('\nThere are ' + str(n) + ' on the board.')
        while player_one < 1 or player_one > 3:
            player_one = int(input('Player 1: How many do you take (1-3)? '))
        n -= player_one
        player_one = 0
        if n < 1:
            print('Player 1 loses.')
            break
        print('\nThere are ' + str(n) + ' on the board.')
        while player_two < 1 or player_two > 3:
            player_two = int(input('Player 2: How many do you take (1-3)? '))
        n -= player_two
        player_two = 0
        if n < 1:
            print('Player 2 loses.')
            break


def human_vs_ai(n, memory=[]):
    sticks = n
    player = 0
    ai = 0
    for i in range(n):
        memory.append([1, 2, 3])
    while True:
        n = sticks
        choices = {}
        while True:
            print('\nThere are ' + str(n) + ' sticks on the board.')
            while player < 1 or player > 3:
                player = int(input('Player: How many do you take (1-3)? '))
            n -= player
            player = 0
            if n < 1:
                print('Player loses.')
                for key in choices:
                    memory[key - 1].append(choices[key])
                    memory[key - 1].append(choices[key])
                break
            print('\nThere are ' + str(n) + ' sticks on the board.')
            ai = random.choice(memory[n-1])
            memory[n-1].remove(ai)
            choices[n] = ai
            print(choices)
            print('AI selects ' + str(ai) + '.')
            n -= ai
            if n < 1:
                print('AI loses.')
                for n in range(len(memory)):
                    if len(memory[n]) < 3:
                        memory[n] = [1, 2, 3]
                break
        print()
        if input('\nPress 0 to exit, anything else to keep playing: ') == '0':
                break


def ai_training(n):
    memory = []
    sticks = n
    ai_smart = 0
    ai_rand = 0
    # create ai_smart's memory
    for i in range(n):
        memory.append([1, 2, 3])
    # play the game 200000 times
    for n in range(200000):
        n = sticks
        choices = {}
        # loop until one ai loses
        while True:
            # ai_rand chooses
            ai_rand = random.randint(1, 3)
            n -= ai_rand
            # ai_smart wins; update memory
            if n < 1:
                for key in choices:
                    memory[key - 1].append(choices[key])
                    memory[key - 1].append(choices[key])
                break
            # ai_smart chooses
            ai_smart = random.choice(memory[n - 1])
            memory[n - 1].remove(ai_smart)
            choices[n] = ai_smart
            n -= ai_smart
            # ai_smart loses; make sure each set of choices contains
            # at least one of each choice
            if n < 1:
                for n in range(len(memory)):
                    if len(memory[n]) < 3:
                        memory[n] = [1, 2, 3]
                break
    print('Training complete.')
    human_vs_ai(sticks, memory)

num_sticks = 0
print('Welcome to the game of sticks!')
while num_sticks < 10 or num_sticks > 100:
    num_sticks = int(input('Choose a number of sticks between 10 and 100: '))

play_game = True

while play_game:
    game_mode = -1
    while game_mode < 0 or game_mode > 3:
        time.sleep(.25)
        print('\nChoose a game mode:')
        print('\tHuman vs human (1)')
        print('\tHuman vs a new AI (2)')
        print('\tHuman vs a trained AI (3)')
        print('\tQuit (0)')
        game_mode = int(input())
    if game_mode == 0:
        break
    elif game_mode == 1:
        human_vs_human(num_sticks)
        continue
    elif game_mode == 2:
        human_vs_ai(num_sticks)
        continue
    elif game_mode == 3:
        ai_training(num_sticks)
        continue
    else:
        break

print('\nThanks for playing!')