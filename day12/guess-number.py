#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


answer = random.randint(0,100)

# TODO-2
# Set attempts based on select difficulty
game_modes = {
    'easy': 10,
    'hard': 5
}

# TODO-1
# Ask user for easy or hard version
def set_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty in game_modes:
            attempts = game_modes[difficulty]
            break
        else:
            print("Chosen difficulty unavailable. ")
    return attempts


# TODO-3
# Prompt user for guess and loop untill out of attempts or a correct guess
def user_guess():
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    return guess

def check_guess(guess,answer):
    if guess > answer:
        print("Too high.\nGuess again.")
    elif guess < answer:
        print("Too low.\nGuess again.")

guess = -1
attempts = set_difficulty()

while guess != answer and attempts >0:
    guess = int(user_guess())
    attempts -=1
# TODO-4
# Tell the user whether they are high or low
    check_guess(guess,answer)

if guess == answer:
    print("You won!")
else:
    print(f"You lost!\nThe answer was {answer}!")