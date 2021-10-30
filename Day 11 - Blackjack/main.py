############### Aaron's Blackjack Project Day 11/100 of Python ######################

import os
from art import logo
import random
#recursive function
def blackjack():
    
    def clear_console():
        os.system('cls')
    clear_console()
    print("Welcome to Aaron's Blackjack!")
    print(logo)
    #card deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #users and dealers card list
    user_cards = []
    computer_cards = []
    #function to calculate an 11 or 1 in ace card, if over 21 then ace becomes 1
    def ace():
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
            

        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
            

    #deal card function that adds random cards to user and dealers decks
    def deal_card():            
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        
        return user_cards, computer_cards

    #totaling the sums of user and dealers cards and calculating scores, game will continue until one of the players are over 21, or until user stands
    def calculate_score(user_cards, computer_cards):    
        user_sum = sum(user_cards)
        computer_sum = sum(computer_cards)      

        if user_sum < 21:
            draw = True
            while draw:

                if user_sum == 21:
                    print('You Win!!!')        
                    draw = False

                if computer_sum == 21:
                    print('You Lose!!!')        
                    draw = False

                draw_another = input('\nWould you like to draw another card? Type y or n: ')

                if draw_another == 'y':                
                    user_cards.append(random.choice(cards))              
                    ace()
                    user_sum = sum(user_cards)
                    print(f'\nYour new cards are: {user_cards}, a total of: {user_sum}')
                            
                while computer_sum < 17:
                    computer_cards.append(random.choice(cards))
                    ace()
                    computer_sum = sum(computer_cards)
                    print(f"The dealer draws: {computer_cards} For a total of: {computer_sum}")
                else:
                    print('The Dealer stays.')

                if user_sum > 21:
                    print('\nYou lose!!!')
                    draw = False

                elif computer_sum > 21:
                    print('\nYou win!!!')
                    draw = False
                
                if draw_another == 'n':
                    if user_sum > computer_sum and user_sum <= 21:
                        print('\nYou win!!!')
                        draw = False
                    elif computer_sum > user_sum and computer_sum <= 21:
                        print('\nYou lose!!!')
                        draw = False
                    elif computer_sum == user_sum:
                        print('\nDraw!!!')
                        draw = False

                if draw == False:
                    play_again = input('Would you like to play again? Type y or n: ')
                    if play_again == 'y':
                        blackjack()




        
        return user_sum, computer_sum


    deal_card()
    print(f"Your cards are: {user_cards} For a total of: {sum(user_cards)}\nThe Dealer's cards are: {computer_cards} For a total of: {sum(computer_cards)}")
    calculate_score(user_cards, computer_cards)
blackjack()

