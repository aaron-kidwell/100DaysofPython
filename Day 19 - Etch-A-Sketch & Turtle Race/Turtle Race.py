# Day 19/100 Python Turtle Race
from turtle import Turtle, Screen
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
race = False
# Set screen size
screen = Screen()
screen.setup(width=500, height=400)

# init list of all turtles appended from following for loop
turtles = []
# set color of turtles for each color then move to starting position
y = -150
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y)
    y += 50
    turtles.append(new_turtle)
# place bets
user_bet = screen.textinput(title='Place your bets', prompt='Which turtle will win the race? Enter a color: ')

# once user bets
if user_bet:
    race = True

    while race == True:
        # race until turtle crosses the finish line, outputs winner in console
        for turtle in turtles:
            if turtle.xcor() > 230:
                race = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've Won! The winner was {winner}.")
                    
                else:
                    print(f"You lost! The winner was {winner}.")                    
            # turtles will move random distances until x = 230
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()