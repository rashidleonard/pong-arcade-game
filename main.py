import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
PADDLES = [(-350, 0), (350, 0)]

X = 350
Y = 0
UP = 90
DOWN = 270
game_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade game")
screen.tracer(0)

l_paddle = Paddle(PADDLES[0])
r_paddle = Paddle(PADDLES[1])
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_on:
    screen.update()
    time.sleep(0.1)  #over here, i tried to make the value less than 0.1 everytime the ball hits so the game can be
    # fast and fun the pad but i get an error: float object not callable. I should come back to it and solve it.
    ball.refresh()

    # detects collision  with top wall and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.fast()

    # when right paddle misses
    if ball.xcor() > 400:
        ball.reset()
        score.left_hand_score()

    # when left paddle misses
    if ball.xcor() < -400:
        ball.reset()
        score.right_hand_score()


screen.exitonclick()
