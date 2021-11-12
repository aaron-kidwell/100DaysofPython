# Day 18/100 Dot Painting
from turtle import Turtle, Screen, colormode
import random

# color list was generated from extracting rgb colors from a Damien Hurst painting using colorgram.py to create a similar auto generated dot painting
color_list = [(239, 239, 238), (233, 237, 233), (235, 236, 240), (242, 234, 237), (43, 105, 171), (233, 206, 116), (225, 152, 87), (183, 50, 77), (118, 87, 50), (228, 120, 147), (214, 61, 80), (109, 110, 188), (130, 175, 210), (115, 185, 139), (55, 176, 110), (116, 168, 37), (202, 18, 42), (33, 56, 113), (221, 61, 50), (26, 142, 108), (154, 222, 193), (181, 170, 221), (30, 163, 170), (84, 35, 39), (40, 46, 80), (233, 167, 180), (237, 172, 162), (76, 40, 39), (154, 208, 221), (115, 46, 43)]

# turtle class, object tim
tim = Turtle()
colormode(255)
tim.speed('fastest')
tim.penup()

x = -450
y = -375

# drawing random colored dots until the y coordinate reaches the top of the page
while y < 400:    
    tim.setpos(x, y)
    y += 50

    for _ in range(18):
        tim.color(random.choice(color_list))       
        tim.dot(20)
        tim.forward(50)     
        tim.dot(20)
    
screen = Screen()
screen.exitonclick()
