# --------------------------------------
# CSCI 127, Lab 2
# September 12, 2017
# Your Name
# --------------------------------------

import turtle

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.goto(-300, 300)
border.down()
for side in range(4):
    border.forward(600)
    border.right(90)

lollipop = turtle.Turtle()
lollipop.color("red")
lollipop.hideturtle()
lollipop.speed(0)

stick = turtle.Turtle()
stick.color("black")
stick.width(5)
stick.hideturtle()
stick.speed(0)
stick.right(90)

""" 
Do not delete or change any of the Python statements above this line.

The next 4 statements illustrate a lollipop of radius 30 whose bottom 
is at (0,0) and a stick of length 60 whose top appears at (0, 0)
"""

import random

def draw_lollipop():
    l = random.randint(10,30)
    x = random.randint(-270, 270)
    y = random.randint(-240, 240)
    lollipop.up()
    lollipop.goto(x,y)
    lollipop.goto
    lollipop.begin_fill()
    lollipop.circle(l)
    lollipop.end_fill()
    stick.up()
    stick.goto(x,y)
    stick.down()
    stick.forward(2*l)

for i in range(1000):
    draw_lollipop()
    





