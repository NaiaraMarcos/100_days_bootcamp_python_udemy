#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
code1 = ''
print(random.choice(letters))
for _ in range(nr_letters):
  code1 += random.choice(letters)
for _ in range(nr_symbols):
  code1 += random.choice(symbols)
for _ in range(nr_numbers):
  code1 += random.choice(numbers)
print(f"Your password is: {code1}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_elements = ['L'] * nr_letters + ['N'] * nr_numbers + ['S'] * nr_symbols
code2 = ''

for _ in range(len(list_elements)):
  rnd_val = random.choice(list_elements)
  if rnd_val == 'L':
    code2 += random.choice(letters)
    list_elements.remove('L')
  elif rnd_val == 'N':
    code2 += random.choice(numbers)
    list_elements.remove('N')
  elif rnd_val == 'S':
    code2 += random.choice(symbols)
    list_elements.remove('S')

print(f"Your password is: {code2}")
