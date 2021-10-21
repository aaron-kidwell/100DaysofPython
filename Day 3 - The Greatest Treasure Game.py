# This is a game I have created as a result of the things I have learned on day 3.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#print intro
print("Welcome to The Greatest Treasure.")
print("Your mission is to investigate the chest.") 
choice1 = input('\nYou come across a mysterious chest. Type "open" or "leave" ')
choice1 = choice1.lower()
#initial choices, the game can end here based on choice.
if choice1 == 'leave' or choice1 != 'open':
  print('\nYou have chosen to walk away, the story does not continue.')
#if statements based on decision to open the chest, begins the game.
if choice1 == 'open':
  choice2 = input('\nYou open the chest and are blinded by a glowing light.\nType "reach" or "close chest". ')
  choice2 = choice2.lower()
  if choice2 == 'close chest' or choice2 != 'reach' :
    print('\nYou cannot close the chest and the light consumes you. You have died.') 
# continuing the game if the correct choices are made
  if choice2 == 'reach':
    print('\nYou reach for the light and become unconscious. You wake up and forget who you are.')
    choice3 = input('\nYou do not know where you are. You see a river and a road.\nType "go to river" or "go to road" ')
    choice3 = choice3.lower()
  # wrong choice made with an additional choice included
  if choice3 != 'go to river' and choice3 != 'go to road':
      print('\nYou failed to make a decision, a mistake from your previous life, the light consumes you and you have died.')
     
  if choice3 == 'go to river':
    choice3a = input('\nYou walk to the river, the water is dark and reflective. You are thirsty.\nType "drink" or "see reflection". ')
    choice3a = choice3a.lower()
    
    if choice3a == 'drink':
      print('\nYou violently consume the water... You feel ill. You die from the poison.')
    elif choice3a == 'see reflection' or choice3a != 'drink':
      print('\nYou stare into the reflection of the water and see you are not yourself. You die from terror.')
# end of game.
  if choice3 == 'go to road':
    print('\nYou discover you are someone else. You start a new life and correct your previous mistakes.')
