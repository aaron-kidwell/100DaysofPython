#This is my hangman game for Day 7/100 of Python.

import random
#ASCII Art as a list, each wrong letter will call from the list until game is over
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# wordlist, randomization
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#intro
print("Welcome to Aaron's Hangman using Python!\n")



#once reaches 0, game is over
lives = 6

#printing the '_' based on the length of the randomly chosen word
display = []
for _ in range(word_length):
    display += "_"
#while loop runs until the display no longer contains '_', meaning the user has won the game, while loops will also stop once no lives are remaining
while not end_of_game:
    guess = input("Guess a letter: ").lower()

   
    for position in range(word_length):
        letter = chosen_word[position]
  
        if letter == guess:
            display[position] = letter
   

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True            

    print(f"{' '.join(display)}")
#switch for while loop
    if "_" not in display:
        end_of_game = True
        print("You win.")

#printing ascii art per life
    if lives == 6:
        print(stages[6])
    if lives == 5:
        print(stages[5])
    if lives == 4:
        print(stages[4])
    if lives == 3:
        print(stages[3])
    if lives == 2:
        print(stages[2])
    if lives == 1:
        print(stages[1])
    if lives == 0:
        print(stages[0])
        print('YOU LOSE!')
    