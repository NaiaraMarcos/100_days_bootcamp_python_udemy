from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data_sneak.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}  |  High_Score = {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open("data_sneak.txt", mode="w") as file:
                file.write(str(self.score))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER\n\n", move=False, align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.write(f"You beat the new record!!!", align=ALIGNMENT, font=FONT)
