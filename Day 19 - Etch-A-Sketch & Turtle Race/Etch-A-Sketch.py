# Day 19/00 Etch-A-Sketch
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# using w, a, s, d, c: clear screen and movements
def move_forwards():
    tim.forward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def move_backwards():
    tim.back(10)    

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
  
# event listener for inputs
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='c', fun=clear_screen)
   
screen.exitonclick()