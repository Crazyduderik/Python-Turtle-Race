import turtle
import time

from turtle import Turtle, Screen
import random

def create_turtles(colors):
    turtles = []
    x = -220
    y = -100
    for color in range(len(colors)):
        todd = Turtle(shape="turtle")
        todd.color(colors[color])
        todd.penup()
        todd.goto(x=x, y=y)
        y += 40
        turtles.append(todd)
    return turtles

def create_finish_line():
    finish_line = Turtle()
    finish_line.pensize(2)
    finish_line.penup()
    finish_line.goto(220,150)
    finish_line.pendown()
    finish_line.goto(220, -150)
    finish_line.hideturtle()
        
screen = Screen()
screen.bgcolor("lightblue")
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
is_race_on = False

while user_bet not in colors:
    user_bet = screen.textinput(title="Invalid Color", prompt="Please enter a valid color (red, orange, blue, green, yellow, purple): ")

turtles = create_turtles(colors)
create_finish_line()

if user_bet:
    for i in range(3,0,-1):
        print(f"Race starts in {i} seconds")
        time.sleep(1)
    is_race_on = True

while is_race_on:
    for turtle in turtles:

        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()