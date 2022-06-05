from turtle import Turtle

YPOS = [230,210,190]
color = "white"

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()

        self.pdd = []
        for item in range(len(y)):
            pd = Turtle(shape="square")
            pd.color(color)
            pd.penup()
            pd.goto(x, y[item])
            self.x = x
            self.y = y[item]
            self.pdd.append(pd)

    def Up(self):
        for item in self.pdd:
            new_x =item.xcor() 
            new_y = item.ycor() + 40
            item.goto(new_x, new_y)

    def Down(self):
        for item in self.pdd:
            new_x = item.xcor() 
            new_y = item.ycor() - 40
            item.goto(new_x, new_y)


# English
# weak students background knowledge
# books