## Day 14/100 Python. Higher/Lower Game

from game_data import data
import random
from art import logo, vs
import os
name1 = random.choice(data)
name2 = random.choice(data)

def clear():
    os.system('cls')
# compares the follower count from game_data, then compares against users input.
def compare():
    global name1, name2
    #setting condition for while loop
    game_continue = True
    #keeping the user's score
    score = 0
    #continously compare game data against users guess until incorrect
    while game_continue:     
        a = name1['follower_count']
        b = name2['follower_count']
        print("\nWelcome to Aaron's Higher/Lower Game!")         
        print(logo)
        print(f"Compare A: {name1['name']}, a {name1['description']}, from {name1['country']}.")
        print(vs)
        print(f"Compare B: {name2['name']}, a {name2['description']}, from {name2['country']}.")
        guess = input("\nWho has more followers on Instagram? Type 'A' or 'B': ")
        guess = guess.lower()
        #if guess is correct, name2 becomes name1 and game will progress
        if guess == 'a' and a > b:
            score += 1
            clear()
            print(f"You're right! Current score: {score}.")
            name1 = name2
            reshuffle()
        elif guess == 'b' and b > a:
            score += 1
            clear()
            print(f"You're right! Current score: {score}.")
            name1 = name2
            reshuffle()
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False

#shuffles the dictionary after a users correct guess, replaces name2.
def reshuffle():
    global name1, name2
    while name1['follower_count'] == name2['follower_count']:        
        name2 = random.choice(data)        


reshuffle()
compare()










