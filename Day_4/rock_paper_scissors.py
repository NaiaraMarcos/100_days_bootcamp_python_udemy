import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
features_game = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice = int(user_choice)

if user_choice >= 3 or user_choice < 0:
  print('Your choice is not correct, you must choose between 0 and 2.')
else:
  print("You choose:\n")
  print(features_game[user_choice])
  print("The computer choose:\n")
  print(features_game[computer_choice])
  
  if user_choice == 0 and computer_choice == 2:
    print("You win!!!")
  elif user_choice == 2 and computer_choice == 0:
    print("Computer wins.")
  elif user_choice > computer_choice:
    print("You win!")
  elif user_choice < computer_choice:
    print("Computer wins.")
  else:
    print('It is a draw!!!')


