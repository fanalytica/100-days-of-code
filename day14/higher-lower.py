# TODO-0
# Break down problem
# TODO-Obj
# Create a game that shows the user two choices and they have to choose which option has more followers

from game_data import data
from art import logo, vs
import random

# TODO-1
# Introduce game
print(logo)

rand_a = random.randint(0,len(data)-1)
rand_b = random.randint(0,len(data)-1)

choice_a = data[rand_a]
choice_b = data[rand_b]

score = 0

# TODO-2 
# Randomly present two options for the user
print(f" Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")

print(vs)

print(f" Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
# TODO-3
# Prompt the user to guess


guess = input("Who has more followers? Type 'A' or 'B': ")

choice_list = [choice_a,choice_b]

# TODO-4
# Determine if they are corret
# If incorrect end game
# If correct continue using the correct guess and compare to another random option
# Present the new choices to the user, repeat

winner = max(choice_list, key= lambda x:x['follower_count'])

if winner == guess:
    score += 1
    print("You're right! Current score: {score}.")
else:
    print("Game over. Final score was {score}.")


