from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

state = True

def custom_input(user_input):
    user_input = input(user_input)
    if user_input == "off":
        print("Shutting down..")
        sys.exit()
    elif user_input == "report":
        money_machine.report()
        coffee_machine.report()
    return user_input


coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while state:
    ordered_item = Menu()
    order = custom_input(f"What would you like? {ordered_item.get_items()}: ")
    if ordered_item.find_drink(order):
        ordered_item = ordered_item.find_drink(order)
        if coffee_machine.is_resource_sufficient(ordered_item):
            input(f"Please pay ${ordered_item.cost}")
            if money_machine.make_payment(ordered_item.cost):
                coffee_machine.make_coffee(ordered_item)






