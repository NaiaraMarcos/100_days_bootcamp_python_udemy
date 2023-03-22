import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Turtle collides with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Turtle reach the top edge
    if player.is_at_finish_line():
        # Maximum level 10
        if scoreboard.level <= 10:
            scoreboard.increase_level()
            player.initial_position()
            car_manager.level_up()
        else:
            scoreboard.pass_all_levels()

screen.exitonclick()
