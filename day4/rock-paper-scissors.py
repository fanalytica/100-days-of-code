rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
pchoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

game = [rock,paper,scissors]
pchoice = int(pchoice)
print(game[pchoice])

print("Computer chose:\n")
cchoice = random.randint(0,2)
print(game[cchoice])
lose = "You lose."
win = "You win."
draw = "It's a draw."

if pchoice == 0 and cchoice== 1:
    print(lose)
elif pchoice == 1 and cchoice == 2:
    print(lose)
elif pchoice == 2 and cchoice == 0:
    print(lose)
elif pchoice == cchoice:
    print(draw)
else:
    print(win)

#always lose
# if pchoice == 0:
#     print(game[1])
# elif pchoice == 1:
#     print(game[2])
# elif pchoice == 2:
#     print(game[0])
