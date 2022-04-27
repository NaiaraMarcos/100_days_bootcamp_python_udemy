from Day_10.art import logo
from replit import clear

# add function
def add(n1, n2):
    return (n1 + n2)
# subtract fuction
def subtract(n1, n2):
    return (n1 - n2)
# multiply
def multiply(n1, n2):
    return (n1 * n2)
# divide
def divide(n1, n2):
    if n2 == 0:
        return "error dividend has to be different than 0"
    else:
        return (n1 / n2)

def calculator():
    print(logo)
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    num1 = float(input("What is the first number? "))
    for operation in operations:
        print(operation)

    continue_calculating = True
    while continue_calculating == True:
        symbol_operation = input("Pick an operation from line above: ")
        num2 = float(input("What is the second number? "))
        function_operation = operations[symbol_operation]
        result = function_operation(num1,num2)
        print(f"{num1} {symbol_operation} {num2} = {result}")
        continue_calc = input("Type 'y' to continue calculing, or type 'n' to start new calculation or 'exit' if you do not want to calculate anything else: ")
        if continue_calc == 'n':
            continue_calculating = False
            clear()
            calculator()
        elif continue_calc == 'y':
            num1 = result
        else:    
            return None
calculator()