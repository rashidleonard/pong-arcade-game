from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pos = 10
        self.y_pos = 10
        self.fast = 0.1
        # self.goto(self.x_pos, self.y_pos)

    def refresh(self):
        x = self.xcor() + self.x_pos
        y = self.ycor() + self.y_pos
        self.goto(x, y)

    def bounce_y(self):
        self.y_pos *= -1

    def bounce_x(self):
        self.x_pos *= -1
        self.fast *= 0.8  # I should come back and solve this error. check main for ref

    def reset(self):
        self.goto(0, 0)
        self.fast = 0.1
        self.bounce_x()
