

from turtle import Turtle
from score import Score
# from main import right_paddle
score = Score()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#fff")
        self.penup()
        self.goto(0, 0)
        self.xmove = 20
        self.ymove = 20
        
    def movement(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_top_bottom(self):
        if self.ycor() >= 250 or self.ycor() <= -250:
            self.ymove *= -1

    def bounce_right_paddle(self):
        self.xmove *= -1

    # def bounce_left_paddle(self):
        
    #     self.xmove *= -1

    def bounce_right(self):
        if self.xcor() >= 410:
            self.xmove *= -1
            score.increase_sscore()

    def bounce_left(self):
        if self.xcor() <= -410:
            self.xmove *= -1
            score.increase_fscore()











