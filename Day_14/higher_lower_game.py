from Day_14.art import logo, vs
from Day_14.game_data import data
from replit import clear
import random


def random_instagramers(data):
    n_instagramers = len(data)
    random_number = random.randint(0, n_instagramers - 1)
    return data[random_number]
    
def comparing_followers(instagramer_1, instagramer_2):
    if instagramer_1['follower_count'] > instagramer_2['follower_count']:
        return('A')
    else:
        return('B')
    
def higher_lower_game():

    print(logo)

    #choosing the first instagramer 
    instagramer_1 = random_instagramers(data)
    score = 0
    game_over = False
    
    while not game_over:
    
        #choosing the second instagramer 
        #Note: Both instagramers have to be different 
        instagramer_2 = random_instagramers(data)
        while instagramer_2['name'] == instagramer_1['name']:
            instagramer_2 = random_instagramers(data)
            
        print(f"Compare A: {instagramer_1['name']}, a {instagramer_1['description']}, from {instagramer_1['country']}.")
        print(vs)
        print(f"Compare B: {instagramer_2['name']}, a {instagramer_2['description']}, from {instagramer_2['country']}.")

        answer = (input("Who has more followers? Type 'A' or 'B'. ")).upper()
        
        clear()
        print(logo)

        if answer == comparing_followers(instagramer_1, instagramer_2):
            score += 1
            print(f"You are right! Your current score: {score}")
            instagramer_1 = instagramer_2

        else:
            print(f"Sorry but this is wrong! Your score: {score}")
            game_over = True

    if (input("Would you like to play again? Type 'y' or 'n'. ")).lower() == 'y':
        higher_lower_game()
    else:
        return None

higher_lower_game()