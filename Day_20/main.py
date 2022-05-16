from turtle import Screen
import time
from sneak import Sneak
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("the famous Snake game")

# Type of game
borders = screen.textinput("Border",
                           "Type yes (with borders) or no (without borders).")
game_speed = screen.textinput("Game speed", "How would you like the speed of the game? (slow/regular/fast")
speed = {'slow': 0.5, 'regular': 0.35, 'fast': 0.09}

sneak = Sneak()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=sneak.up)
screen.onkey(key="Down", fun=sneak.down)
screen.onkey(key="Right", fun=sneak.right)
screen.onkey(key="Left", fun=sneak.left)

games_is_on = True
while games_is_on:
    screen.update()
    time.sleep(speed[game_speed.lower()])
    sneak.move()

    # Detect collision with the food
    if sneak.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        sneak.extend()
    # Detect collision with the walls
    if borders.lower() == 'yes':
        if sneak.head.xcor() > 280 or sneak.head.xcor() < - 280 or \
                sneak.head.ycor() > 280 or sneak.head.ycor() < -280:
            games_is_on = False
            scoreboard.reset()
            scoreboard.game_over()
    elif borders.lower() == 'no':
        if sneak.head.xcor() >= 290:
            sneak.head.setx(-300)
        elif sneak.head.xcor() <= -290:
            sneak.head.setx(300)
        elif sneak.head.ycor() >= 290:
            sneak.head.sety(-300)
        elif sneak.head.ycor() <= -290:
            sneak.head.sety(300)
    # Detect collision with the tail
    for segment in sneak.segments[1:]:
        if sneak.head.distance(segment) < 10:
            games_is_on = False
            scoreboard.game_over()

screen.exitonclick()
