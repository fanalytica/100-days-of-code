#Completed in replit.com

import art
# from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

print("Welcome to the secret auction program.")

run_state = True
bid_collection = []
max_bid = 0
max_bidder = ""
while run_state is True:
  name = input("What is your name?: ")
  bid = float(input("What's your bid?: $"))

  bid_collection.append({"name": name, "bid": bid})

  user_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if 'y' in user_continue[0]:
    run_state = True
    # clear()
  else:
    run_state = False

if run_state is False:
  for name in bid_collection:
    if name["bid"] > max_bid:
      max_bid = name["bid"]
      max_bidder = name["name"]
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")
