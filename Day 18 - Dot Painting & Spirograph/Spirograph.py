# Day 18/100 Random Walk
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
tim.speed('fastest')

# function to generate random rgb colors
def random_colors():
    global colors
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# draws circles and turns cursor slightly until the image of spirograph is completed
for _ in range(100):
    tim.color(random_colors())
    tim.circle(100)
    tim.right(5)
    
screen = Screen()
screen.exitonclick()




