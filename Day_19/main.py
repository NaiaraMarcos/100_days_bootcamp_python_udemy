from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.title("The turtle race")
user_bet = screen.textinput(title="Make your bet", prompt="What turtle will win the race? Enter the colour: ")

color_turtle = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
# position y exe.
y_position = -70
for color in color_turtle:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-240, y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            turtle_winning = turtle.pencolor()
            if turtle_winning == user_bet:
                print(f"You win!!! The {turtle_winning} turtle is the winner!")
            else:
                print(f"You lose!!! The {turtle_winning} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
