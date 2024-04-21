#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_size =  nr_letters + nr_symbols + nr_numbers
password=""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for n in range(nr_letters):
#     password += letters[random.randint(0,len(letters)-1)]
# for n in range(nr_symbols):
#     password+= symbols[random.randint(0,len(symbols)-1)]
# for n in range(nr_numbers):
#     password += numbers[random.randint(0,len(numbers)-1)]

# print(f"Your weak password is: {password} with length {len(password)}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for n in range(total_size):
    pick_char = random.randint(0,2)
    if (pick_char == 0 and nr_letters == 0) or (pick_char == 1 and nr_symbols == 0) or (pick_char == 2 and nr_numbers == 0):
        pick_char = (pick_char+1) % 3
    elif pick_char == 0 and nr_letters > 0:
        password += letters[random.randint(0,len(letters)-1)]
        nr_letters -= 1
    elif pick_char == 1 and nr_symbols > 0:
        password+= symbols[random.randint(0,len(symbols)-1)]
        nr_symbols -= 1
    elif pick_char == 2 and nr_numbers > 0:
        password += numbers[random.randint(0,len(numbers)-1)]
        nr_numbers -= 1


print(f"Your strong password is: {password} with length {len(password)}")