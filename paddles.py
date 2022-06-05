from turtle import Turtle

LONG_OF_PADDLES = 5
SPEED_OF_PADDLES = 45

MOVE_UP = 90
MOVE_DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(1, 1 * LONG_OF_PADDLES)
        self.setheading(MOVE_UP)
        self.penup()
        self.color("white")
        self.goto(position)


    def Up(self):
        self.setheading(MOVE_UP)
        self.forward(SPEED_OF_PADDLES)


    def Down(self):
        self.setheading(MOVE_DOWN)
        self.forward(SPEED_OF_PADDLES)

    # def W_key(self):
    #     for item in self.left_paddle:
    #         item.setheading(MOVE_UP)
    #         item.forward(SPEED_OF_PADDLES)
    

    # def S_key(self):
    #     for item in self.left_paddle:
    #         item.setheading(MOVE_DOWN)
    #         item.forward(SPEED_OF_PADDLES)


# class Right_paddle():
#     def __init__(self):

#         self.right_paddle = []
#         self.create_right_paddle()

#     def create_right_paddle(self):
#         i = 0
#         for item in range(LONG_OF_PADDLES):
#             item = Turtle(shape="square")
#             item.speed("fastest")
#             item.penup()
#             item.color("white")
#             item.goto(x = RIGHT_X, y = LEFT_Y[i])
#             i += 1
#             self.right_paddle.append(item)







