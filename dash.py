from turtle import Turtle


class Dashed(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -300)
        self.color("white")
        self.setheading(90)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.hideturtle()
