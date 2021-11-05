from turtle import Turtle
ALLIGNMENT ="center"
FONT =("Arial", 60, "normal")


class ScoreBoard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.n = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.n, align=ALLIGNMENT, font=FONT)

    def increase_the_score(self):
        # increases the score
        self.n += 1
        # clears screen so  that it updates again, and don't get overlap
        self.clear()
        self.update_scoreboard()