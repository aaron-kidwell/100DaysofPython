# Day 12/100 Guess a Number
from random import randint
from art import logo
print("Welcome to Aaron's Guess a Number!")
print(logo)
print("I'm thinking of a number betweeen 1 and 100.")
#Number guessing function
def guess_a_num():
    number = randint(1, 100)
    difficulty = input("Choose a difficult. Type 'easy' or 'hard': ")
    #difficulty dictates amount of lives
    if difficulty == 'easy':
        lives = 10
    else:
        lives= 5
    #while loop continues until continue game is false which is either lives 0 or correct guess
    continue_game = True
    while lives != 0 and continue_game == True:
        
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))

        if guess > number:
            print('Too high.')
            lives -= 1
        elif guess < number:
            print('Too low.')
            lives -= 1
        elif guess == number:
            print(f'You did it! The number was {number}.')
            continue_game = False
        else:
            print('Incorrect input.')
            lives -= 1
    
        if lives == 0:
            print('You have ran out of lives.')
            continue_game = False
#call the function
guess_a_num()