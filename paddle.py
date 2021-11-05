from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.color("white")
        self.penup()
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

