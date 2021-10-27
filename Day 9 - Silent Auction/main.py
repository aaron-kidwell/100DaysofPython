#Day 9/100 Silent Auction
from art import logo
import os
clear = lambda:os.system('cls')
others = True

### dictionary bidders names and amounts will be stored here
bidders = {}
###


#function for finding the highest bid and declaring the winner
def find_highest_bid(bids):
    highest = 0
    winner = ''
    for each in bids:
        amount = bids[each]
        if amount > highest:
            highest = amount
            winner = each
    print(f'The winner is {winner} with a bid of ${highest}!')

#looping collection of inputs if there is multiple bidders, then sending arguments to the find_highest_bid function
while others == True:   
    clear() 
    print(logo)
    name_input = input('What is your name? ')    
    bid_input = int(input('Enter your bid amount: $'))
    bidders[name_input] = bid_input 
    other_bidders = input('Are there other bidders? Type yes or no. ')
    if other_bidders == 'no':
     others = False    
     find_highest_bid(bidders)
    


  

    
        




