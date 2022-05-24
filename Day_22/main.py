from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

score = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with border up and down
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()
    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()
    if score.r_score >= 10 or score.l_score >= 10:
        game_is_on = False
        score.game_over()


screen.exitonclick()