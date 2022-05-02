# this project  is called coffee machine
# it must create the similar function that type of machines does: turn_off, report, serve drinks and return change.
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def amount_insert():
    """Calculate the amount of money insert in the machine"""
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
    total_amount = 0
    for coin in coins:
        n_coin = int(input(f"how many {coin}? "))
        total_amount += n_coin * coins[coin]
    return total_amount


def machine_report(resource):
    """Print all values that there is in the machine"""
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${resource['money']}")


def check_enough_element(menu, resource, beverage):
    """It is checking if the ingredients are sufficient. It returns False if they are insufficient, True otherwise."""
    for elem in menu[beverage]['ingredients']:
        if resource[elem] - menu[beverage]['ingredients'][elem] < 0:
            print(f"Sorry, there is not enough {elem}.")
            return False
    return True


def coffee_machine(menu, resource):
    beverage = (input("What would you like to drink? (espresso/latte/cappuccino): ")).lower()
    if beverage == 'report':
        machine_report(resource)
        coffee_machine(menu, resource)
    elif beverage == 'off':
        return None
    else:
        if not check_enough_element(menu, resource, beverage):
            coffee_machine(menu, resource)
        else:

            cost = menu[beverage]['cost']
            print(f"The beverage costs: {cost}. Please, insert the coins")
            amount_user = amount_insert()
            if amount_user >= cost:
                change = round((amount_user - cost), 2)
                for elem in menu[beverage]['ingredients']:
                    resource[elem] -= menu[beverage]['ingredients'][elem]
                resource['money'] += cost
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Here is your {beverage}. Enjoy ☕️!")
            else:
                print(f"Sorry, it is not enough money. Money refunded: {amount_user}")
            coffee_machine(menu, resource)


coffee_machine(MENU, resources)

