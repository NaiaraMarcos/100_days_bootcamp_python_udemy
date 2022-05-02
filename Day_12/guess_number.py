#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from Day_12.art import logo
from replit import clear

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def level_dificulty():
    difficulty_type = (input("Choose the level of diffilcuty: type 'easy' or 'hard'. ")).lower()
    if difficulty_type == 'easy':
        return (EASY_LEVEL_TURNS)
    else:
        return(HARD_LEVEL_TURNS)
    
def guessing_number ():
    print(logo)   
    print("Welcome to the number guessing game!!!")
    print("I am thinking a number between 1 and 100. Can you guess it?")
    number_secret = random.randint(1,100)
    times_attempts = level_dificulty()
    
    game_over = False
    while times_attempts > 0 and not game_over == True:
        print(f"You have {times_attempts} attempts remaining to try to guess the number. ")
        number_guess = int(input("Make a guess: "))
        if number_guess == number_secret:
            game_over = True
            print(f"You win! Well done you figure it out. The number is {number_secret}.")
        elif number_guess > number_secret:
            print("Too high!!!")
        else:
            print("Too low!!!")
        times_attempts -=1    
        if times_attempts == 0:
            print(f"Ohhh!!! You lose, the number is {number_secret}")

    if (input("Would you like to play again? Type 'y' or 'n'. ")).lower() == 'y':
        clear()
        guessing_number()
    else:
        return None
        

guessing_number()