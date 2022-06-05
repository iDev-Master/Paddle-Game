from turtle import Screen, left, right
from ball import Ball
from paddle import Paddle
# from score import Score
import time

screen = Screen()
screen.setup(width=860, height=540)
screen.colormode(255)
screen.bgcolor(12,90,100)
screen.tracer(0)

LEFT = 0
RIGHT = 0

# turtle = Turtle()
ball = Ball()
# score = Score()

y = [230, 210, 190, 170, 160]
right_paddle = Paddle(380, y)
left_paddle = Paddle(-380, y)









screen.listen()
screen.onkey(right_paddle.Up,  "Up")
screen.onkey(right_paddle.Down, "Down")
screen.onkey(left_paddle.Up, "w")
screen.onkey(left_paddle.Down, "s")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    ball.movement()
    ball.bounce_top_bottom()
    ball.bounce_right()
    ball.bounce_left()
    for item in right_paddle.pdd:
        if ball.distance(item) < 30 and ball.xcor() >= 340:
            time.sleep(.1)
            ball.bounce_right_paddle()

    for item in left_paddle.pdd:
        if ball.distance(item) < 30 and ball.xcor() <= -340:
            time.sleep(.1)
            ball.bounce_right_paddle()



    













screen.exitonclick()