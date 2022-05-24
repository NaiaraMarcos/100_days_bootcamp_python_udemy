from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')
FONT_GAME_OVER = ('Arial', 30, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(100, 0)
        self.color("red")
        if self.r_score > self.l_score:
            self.write(f"Congratulations!!! \nThe right player won with score: {self.r_score} \
                      \nThe left player score: {self.l_score}", align=ALIGNMENT, font=FONT_GAME_OVER)
        elif self.r_score < self.l_score:
            self.write(f"Congratulations!!! \nThe left player won with score: {self.l_score} \
                      \nThe right player score: {self.r_score}", align=ALIGNMENT, font=FONT_GAME_OVER)
        else:
            self.write(f"Congratulations!!! Both players draw with score: {self.l_score}",
                       align=ALIGNMENT, font=FONT_GAME_OVER)
