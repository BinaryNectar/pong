# view.py
import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

class TurtleBall(turtle.Turtle):
    def __init__(self, logic: Ball):
        super().__init__(shape="circle")
        self.logic = logic
        self.penup()
        self.color("white")
        self.goto(logic.x, logic.y)

    def sync(self):
        self.goto(self.logic.x, self.logic.y)

class TurtlePaddle(turtle.Turtle):
    def __init__(self, logic: Paddle):
        super().__init__(shape="square")
        self.logic = logic
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(logic.x, logic.y)

    def sync(self):
        self.goto(self.logic.x, self.logic.y)

class TurtleScoreboard(turtle.Turtle):
    def __init__(self, logic: Scoreboard):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.logic = logic

    def sync(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.logic.l_score, align="center", font=("Arial", 45, "normal"))
        self.goto(100, 200)
        self.write(self.logic.r_score, align="center", font=("Arial", 45, "normal"))