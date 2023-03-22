from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
FONT_GAMEOVER = ("Arial", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.level = 1
        self.update_screen()

    def update_screen(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_GAMEOVER)

    def pass_all_levels(self):
        self.color("red")
        self.goto(0, 0)
        self.write("CONGRATULATIONS!!! \n YOU PASS ALL LEVELS", align=ALIGNMENT, font=FONT_GAMEOVER)

