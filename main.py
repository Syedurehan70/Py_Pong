from turtle import Screen
from dash import Dashed
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=1000)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# creating two same turtle by same class at different position by passing the position as tuples
r_paddle = Paddle((480, 0))
l_paddle = Paddle((-485, 0))
r_score = ScoreBoard((-250, 210))
l_score = ScoreBoard((250, 210))
dashed = Dashed()
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # move class
    ball.move()

    # detecting collision with the horizontal walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 450 or ball.distance(l_paddle) < 50 and ball.xcor() < -450:
        ball.bounce_x()

    # detecting if the ball misses the right paddle
    if ball.xcor() > 495:
        r_score.increase_the_score()
        ball.reset_position()

    # detecting if the ball misses the left paddle
    if ball.xcor() < -495:
        l_score.increase_the_score()
        ball.reset_position()


screen.exitonclick()
