from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()


    def score_update(self):
        self.clear()
        self.goto(x=-115, y=210)
        self.color("white")
        self.write(f"Player A = {self.l_score} | Player B = {self.r_score} ", font=("Arial", 15, "normal"))


    def left_score(self):
        self.l_score += 1
        self.score_update()


    def right_score(self):
        self.r_score += 1
        self.score_update()





