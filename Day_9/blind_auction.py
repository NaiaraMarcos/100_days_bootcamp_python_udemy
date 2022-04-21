from replit import clear
from Day_9.art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

bids = {}
continue_bids = True

def best_bidder(bid_records):
    max_name = ''
    max_bid = 0
    for name in bid_records:
        if bid_records[name] > max_bid:
            max_name = name
            max_bid = bid_records[name]
    print(f"The winner is {max_name} with a bid of ${max_bid}.")

while continue_bids == True:
    name_bid = input("What is your name? ")
    amount_bid = int(input("What\'s your bid? $"))
    bids[name_bid] = amount_bid

    more_biders = (input("Are there other any bidders? Type 'yes' or 'no'.\n" )).lower()
    clear()
    if more_biders == 'no':
        continue_bids = False
        best_bidder(bids)
