from turtle import Turtle

MOVE_X = 10
MOVE_Y = 10
MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.move_x = MOVE_X
        self.move_y = MOVE_Y
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.bounce_x()
