import sys


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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 5
    }

# TODO prompt user input
# Ask for type of coffee
# Dispense if enough money
# repeat

def order_coffee(resources):
    # recvd_input = False
    # while not recvd_input:
    #     order = input("​What would you like? (espresso/latte/cappuccino):​")
    #     if order == 'report':
    #         report_avail_resources(resources)
    #     else: 
    #         recvd_input = True
    #         return order
    order = "​What would you like? (espresso/latte/cappuccino):​"
    order = req_user_input(order,resources)
    return order

# TODO Function to turn off coffee machine
def turn_off():
    sys.exit()

# TODO Report function to show current available resources
# Water, milk, coffee, money
def req_user_input(user_prompt,resources):
    recvd_input = False
    while not recvd_input:
        user_input = input(user_prompt)
        if user_input == 'report':
            print(f"Available resources:\n{resources}")
        elif user_input == 'off':
            turn_off()
        else: 
            recvd_input = True
            return user_input
   



def verify_valid_item(order,resources):
    if order in MENU:
        ordered_item = MENU[order]
        print(f"key = {order} value = {ordered_item}")
    else:
        print("Sorry, we do not have that item available")
        ordered_item = False
    return ordered_item

def calc_remaining_resources(valid_item,resources):
    ingredients = valid_item['ingredients']
    remaining_resources = {}
    for key in ingredients:
        remainder =  resources[key] - ingredients[key]
        if remainder >= 0:
            remaining_resources[key] = remainder
        else:
            remaining_resources[key] = False
    return remaining_resources

# TODO Verify sufficient resources for requested drink

def verify_sufficient_resources(valid_item,resources):
    ingredients = calc_remaining_resources(valid_item,resources)
    for key in ingredients:
        if not ingredients[key]:
            print(f"Not enough {key} available.\n{valid_item['ingredients'][key]} needed.\n{resources[key]} in stock.")
        else:
            print(f"Sufficient {key} resources available.")
    if all(ingredients.values()):
        return ingredients
    else:
        return False

# TODO Request payment
# Prompt user for payment in quarters, dimes, nickles, pennies
def request_payment(user_order,ordered_item,resources):
    print(f"{ordered_item} costs ${user_order['cost']}")
    print("Please insert coins.")
    quarters = int(req_user_input("How many quarters?: ",resources))
    dimes = int(req_user_input("How many dimes?: ",resources))
    nickles = int(req_user_input("How many nickles?: ",resources))
    pennies = int(req_user_input("How many pennies?: ",resources))
    total_payment = quarters*.25 + dimes*.1 + nickles*.05 + pennies*.01
    return total_payment

# TODO Process payment
# Verify sufficent funds provided by user for cost of drink
# If sufficient add cost to machine profits
# If not sufficient refund money
# If too much money return change
def process_payment(payment,user_order,resources):
    change = payment - user_order['cost']
    avail_change= resources['money']
    if change >= 0 and avail_change>=change:
        print(f"Here is ${change} in change.")
        return change
    elif change >=0 and avail_change<change:
        print(f"Sorry only ${avail_change} available to dispense as change.")
        return False
    else:
        print("Insufficient funds provided. Dispensing refund..")
        print(f"Recieved {payment} in change.")
        return False


# TODO Make coffee
# If payment is successfully processed and sufficient resources available  make drink
# Deduct used resources from available resources
# Tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink
def make_drink(resources,remaining_resources,user_order,ordered_item):
    remaining_resources['money'] = -1*user_order['cost']
    new_resources = {key: resources[key] - remaining_resources.get(key,0) for key in resources}
    print(f"Here is your {ordered_item}. Enjoy!")
    return new_resources


def main():
    machine_power = True
    resources = RESOURCES
    while machine_power:
        #
        user_order = order_coffee(resources).lower()
        print(user_order)
        #I should have maintained the structure of the nested dictionary instead of doing this to save the name of the order.
        ordered_item = user_order
        user_order= verify_valid_item(user_order,resources)
        # report_avail_resources(resources)
        remaining_resources = verify_sufficient_resources(user_order,resources)
        # print(remaining_resources)
        if remaining_resources:
            payment = request_payment(user_order,ordered_item,resources)
            change = process_payment(payment,user_order,resources)
            if change is not False:
                resources = make_drink(resources,remaining_resources,user_order,ordered_item)
        else:
            print("Please order a different drink.")
        print(resources)

        
        # while user_order:
        #     for resource in remaining_resources:
        #         if not resource:
        #             print(f"Not enough {resource} for drink.")
        #             user_order = False
        #         else:

                

        



if __name__ == "__main__":
    main()