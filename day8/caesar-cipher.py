alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    try:
      position = alphabet.index(char)
      new_position = (position + shift_amount)%26
      end_text += alphabet[new_position]
    except ValueError:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")
  run_program(True)

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
def run_program(runstate):
  while runstate == True:
    user_continue_input = input("Would you like to encode or decode something else?")
    if 'y' in user_continue_input:
      runstate = False
      get_input()
    elif 'n' in user_continue_input:
      runstate = False
      print("Goodbye.")
    else:
      user_continue_input

def get_input():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  return caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
get_input()
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)