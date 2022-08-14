# A simple user vs computer rock, paper, scissors game
# Computer options:  1-Rock, 2-Paper, 3-Scissors
import random

# Computer's choice
# Return a value of the options dictionary based on the random number generated


def get_comp_choice():
    options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    rand_num = random.randint(1, 3)
    comp_choice = options[rand_num]
    return comp_choice.lower()

# User Choice


def get_user_choice():
    user_input = input('Rock, paper, or scissors?')
    user_input = user_input.lower()
    return user_input

# game result returns a str of 'win', 'lose', or 'draw'


def get_result(user_choice, comp_choice):
    # Rock beats scissors, scissors beat paper, paper beats rock
    if user_choice == comp_choice:
        return f'We have a tie! You both chose {user_choice}'
    elif user_choice == 'rock' and comp_choice == 'scissors':
        return f'You win! {user_choice} beats {comp_choice}'
    elif user_choice == 'paper' and comp_choice == 'rock':
        return f'You win! {user_choice} beats {comp_choice}'
    elif user_choice == 'scissors' and comp_choice == 'paper':
        return f'You win! {user_choice} beats {comp_choice}'
    else:
        return f'You lose! {comp_choice} beats {user_choice}'


# GAME LOGIC
comp_choice = get_comp_choice()

# get input until user enters 'rock', 'paper' or scissors
while True:
    user_choice = get_user_choice()
    if user_choice in ['rock', 'paper', 'scissors']:
        break

result = get_result(user_choice, comp_choice)
print(result)
