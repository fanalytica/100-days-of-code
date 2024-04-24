# TODO-0
# Break down problem
# TODO-Obj
# Create a game that shows the user two choices and they have to choose which option has more followers

from game_data import data
from art import logo, vs
import random

# TODO-1
# Introduce game
def start_game(data):
    print(logo)

    rand_a = random.randint(0,len(data)-1)
    rand_b = random.randint(0,len(data)-1)

    choice_a = data[rand_a]
    choice_b = data[rand_b]

    score = 0
    return choice_a,choice_b

# TODO-2 
# Randomly present two options for the user
def print_vs(choice_a,choice_b):
    print(f" Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

    print(vs)

    print(f" Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
# TODO-3
# Prompt the user to guess

def user_guess():
    guess_input = 0
    guess_list = ['a','b']
    while guess_input not in guess_list:
        try:
            guess_input = input("Who has more followers? Type 'A' or 'B': ").lower()
            guess = guess_list.index(guess_input)
        except:
            print("Not a valid option.")
    return guess


# TODO-4
# Determine if they are corret
# If incorrect end game
# If correct continue using the correct guess and compare to another random option
# Present the new choices to the user, repeat

def compare_guess(winner,guess,score):
    if winner['name'] == guess['name']:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Game over. Final score was {score}.")


def main():
    score = 0
    choice_a,choice_b = start_game(data)
    choice_list = [choice_a,choice_b]
    print_vs(choice_a,choice_b)
    guess_index = user_guess()
    guess = choice_list[guess_index]
    winner = max(choice_list, key= lambda x:x['follower_count'])
    compare_guess(winner,guess,score)

if __name__ == "__main__":
    main()