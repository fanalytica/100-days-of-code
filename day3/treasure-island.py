print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_dir = input("What direction would you like to start?\n")
if first_dir.lower() != 'left':
    print("You begin by turning right and walking.\nYou feel the ground disappear beneath your feet and realize that wasn't the 'right' direction\n Game over.")
else:
    second_dir = input("You begin a light jaunt to your left. Eventually you approach a trench filled with water. What would you like to do?\n")
    if second_dir.lower() != 'wait':
        print("A ferocious school of trout sense your movement and begin soaring towards you at unimaginable speeds. In your last moments you only feel a strange, sudden craving for fish and chips.\nGame over.")
    else:
        third_dir = input("As you finish cleaning your navel while waiting around you suddenly catch a glimpse of something shimmering nearby. You approach the shimmer and a red, blue, and yellow door appear. \nWhich door would you like to open?\n")
        if third_dir.lower() == 'yellow':
            print('Congratz bro you did it')
        elif third_dir.lower() == 'red':
            print('As you turn the knob on the red door a bead of sweat drips down your brow. Oops - you immolated.\n Game over.')
        elif third_dir.lower() == 'blue':
            print("You quickly swing open the blue door and rapidly scan the next area for treasure. In fact, you are so focused on the search for treasure you hardly feel the pain in your legs as three vicious wild boars begin devouring you.\n Game over.")
        else:
            print("'Wait what are you doing?'\n'That's not going to work.'\nYou feel all of reality slip away as your consciousness ceases to exist.\nAll that remains is a distant, echoing voice:\n'We don't have the budget to consider every goddamn lunatic's random decision! Just do the doors and ship it so we can get paid!'\nGame over.")
