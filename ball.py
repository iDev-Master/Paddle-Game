from turtle import Turtle

# middle way
class Midway():
    def __init__(self):

        Y = 160
        for dash in range(7):
            dash = Turtle()
            dash.color("#689")
            dash.shape("square")
            dash.penup()
            dash.goto(0, Y)
            Y -= 60
            dash.shapesize(1.6, .35)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10


    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce(self):    
        self.y_move *= (-1)


    def paddle_colision(self):
        self.x_move *= (-1)


    def right_lose(self):
        self.x_move *= (-1)
        self.goto(0, 0)


    def left_lose(self):
        self.x_move *= (-1)
        self.goto(0, 0)



