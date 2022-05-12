from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_turn_on = True

while is_turn_on:
    options = menu.get_items()
    choice = input(f"What would you like to get? {options}: ")

    if choice == 'off':
        is_turn_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        beverage = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(beverage):
            cost = beverage.cost
            print(f"The {choice} costs: {cost}.")
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(beverage)

