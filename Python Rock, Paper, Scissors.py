#this is my rock paper scissors game. then enemy uses random to choose rock paper or scissors.

#ASCII ART
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
#INTRO, defining enemy input
import random
print("Welcome to Aaron's Rock Paper Scissors Game!\n\n")
choice = int(input('Choose 1 for Rock, 2 for Paper, or 3 for Scissors. Good luck! '))
enemy = random.randint(1, 3)

if choice == 1:
  print(f'{rock} \n You chose Rock!')
elif choice == 2:
  print(f'{paper} \n You chose Paper!')
elif choice == 3:
  print(f'{scissors} \n You chose Scissors!')
else:
  print('\nInvalid input, you lose!')
  
if enemy == 1:
  print(f'{rock} \n The enemy chose Rock!')
elif enemy == 2:
  print(f'{paper} \n The enemy chose Paper!')
elif enemy == 3:
  print(f'{scissors} \n The enemy chose Scissors!')


win = '\n YOU WON!!!'
tie = '\n IT WAS A TIE...PLAY AGAIN!'
lose = '\n YOU WERE DEFEATED...TRY AGAIN!'

if choice == 1 and enemy == 1:
  print(tie)
elif choice == 1 and enemy == 2:
  print(lose)
elif choice == 1 and enemy == 3:
  print(win)

elif choice == 2 and enemy == 1:
 print(win)
elif choice == 2 and enemy == 2:
 print(tie)
elif choice == 2 and enemy == 3:
 print(lose)

elif choice == 3 and enemy == 1:
 print(lose)
elif choice == 3 and enemy == 2:
 print(win)
elif choice == 3 and enemy == 3:
 print(tie)
