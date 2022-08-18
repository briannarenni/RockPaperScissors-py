# Game Class
import random

class Game:
    def __init__(self):
        self.comp_choice = self.get_comp_choice()
        self.user_choice = self.get_user_choice()
        self.result = self.get_result()

    def get_comp_choice(self):
        options = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        random_num = random.randint(1, 3)
        return options[random_num].lower()

    def get_user_choice(self):
        self.user_choice = input('Rock, paper, or scissors?: ')
        return self.user_choice.lower()

    def get_result(self):
        if self.comp_choice == self.user_choice:
            return f'A draw! You both chose {self.comp_choice}'
        elif self.user_choice == 'paper' and self.comp_choice == 'rock':
            return f'You win! {self.user_choice} beats {self.comp_choice}'
        elif self.user_choice == 'rock' and self.comp_choice == 'scissors':
            return f'You win! {self.user_choice} beats {self.comp_choice}'
        elif self.user_choice == 'scissors' and self.comp_choice == 'paper':
            return f'You win! {self.user_choice} beats {self.comp_choice}'
        else:
            return f'You lose! {self.comp_choice} beats {self.user_choice}'

    def print_result(self):
        print(f'Computer chose: {self.comp_choice}')
        print(f'You chose: {self.user_choice}')
        print(self.result)
