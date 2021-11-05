from turtle import Turtle


class Ball(Turtle):

    # creating a ball
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.shape("circle")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # directing the ball towards the coordinates
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # this will change the value of y_move in whole class
        self.y_move *= -1

    def bounce_x(self):
        # this will change the value of x_move in whole class
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
