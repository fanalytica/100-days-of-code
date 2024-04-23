############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

#draw player cards until the pass or bust

#draw dealer cards until they reach 17 or bust

def deal_card(player):
    #Pick a random card from the pool of available cards
    rand_card = random.randint(0,len(cards)-1)
    #should have used random.choice()
    player.append(cards[rand_card])
    #could have pulled this out of the function so the function is only performing the action of dealing a card.
    return player

def calc_score(player):
    score = sum(player)
    global player_continue
    global game_state
    #recalculate ace (11) to 1 if score > 21
    #didn't check for blackjack
    #while loop probably unnecessary
    while score > 21:
        if 11 in player:
            player[player.index(11)]=1
            score = sum(player)
        else:
            player_continue = False
            game_state = False
            print("Hand went over 21!")
            break
    return score

def print_game_state(player,computer):
        # player_score = calc_score(player)
        # computer_score = calc_score(computer)
        print(f"Your cards: {player}, current score: {player_score}")
        if len(computer) == 1:
            print(f"Computer's first card: {computer}")
        else:
            print(f"Computer's cards: {computer}, current score: {computer_score}")


if __name__ == '__main__':

    game_state = True

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_hand = []
    #could have just used my defined function for calculating the score
    player_score = sum(player_hand)

    computer_hand = []
    computer_score = sum(computer_hand)
    
    #deal the first cards
    player_hand = deal_card(player_hand)
    player_hand = deal_card(player_hand)
    computer_hand = deal_card(computer_hand)
    player_continue = True
    computer_continue = True

    while game_state:
        player_score = calc_score(player_hand)
        computer_score = calc_score(computer_hand)

        # print(f"Your cards: {player_hand}, current score: {player_score}")
        # if len(computer_hand) == 1:
        #     print(f"Computer's first card: {computer_hand}")
        # else:
        #     print(f"Computer's cards: {computer_hand}, current score: {computer_score}")
        print_game_state(player_hand,computer_hand)
        
        #Deal for player
        while player_continue:
            player_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_continue == 'n':
                player_continue = False
            # elif player_continue == 'bust':
            #     print("You lose.")
            #     player_continue = False
            #     game_state = False
            else:
                player_hand = deal_card(player_hand)
                player_score = calc_score(player_hand)
                print_game_state(player_hand,computer_hand)
        #Deal for computer
        while computer_score < 17 and game_state:
            computer_hand = deal_card(computer_hand)
            computer_score = calc_score(computer_hand)
            print_game_state(player_hand,computer_hand)
        
        print("Game over.")
        game_state = False
        
    
#could have put this in a function
if player_score > 21:
    print("Dealer won!")
elif computer_score > 21:
    print("Player won!")
elif player_score > computer_score:
    print("Player won!")
elif computer_score > player_score:
    print("Computer won!")
else:
    print("Draw.")

#Didn't add option to restart the game
#Would need to do new while loop and put all the code with the actual game steps in to the while loop for as long as the player keeps choosing to play again

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

