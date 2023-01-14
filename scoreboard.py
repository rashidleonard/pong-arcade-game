from turtle import Turtle

FONT = ("Courier", 25, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(arg=f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(arg=f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def left_hand_score(self):
        self.left_score += 1
        self.update_score()

    def right_hand_score(self):
        self.right_score += 1
        self.update_score()
