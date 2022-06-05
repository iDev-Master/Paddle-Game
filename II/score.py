from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#789")
        self.hideturtle()
        self.fscore = 0
        self.sscore = 0
        self.new_score()
    
    def new_score(self):
        self.clear()
        self.penup()
        self.goto(-95, 220)
        self.write(f"First player: {self.fscore} | Second player: {self.sscore}", -25, font=("Arial", 12, "normal"))

    def increase_fscore(self):
        self.fscore += 1
        self.new_score()

    def increase_sscore(self):
        self.sscore += 1
        self.new_score()
