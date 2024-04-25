MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO prompt user input
# Ask for type of coffee
# Dispense if enough money
# repeat

# TODO Function to turn off coffee machine

# TODO Report function to show current available resources
# Water, milk, coffee, money

# TODO Verify sufficient resources for requested drink

# TODO Request payment
# Prompt user for payment in quarters, dimes, nickles, pennies

# TODO Process payment
# Verify sufficent funds provided by user for cost of drink
# If sufficient add cost to machine profits
# If not sufficient refund money
# If too much money return change

# TODO Make coffee
# If payment is successfully processed and sufficient resources available  make drink
# Deduct used resources from available resources
# Tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink
