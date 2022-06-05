from turtle import Screen
from score import Score
from paddles import Paddle
from ball import Midway, Ball
import time

#    The background
screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("#122223")
screen.title("Ping Pong")
screen.tracer(0)     # animation off

# all parts of the game
right_paddle = Paddle((355, 150))
left_paddle = Paddle((-355, 150))
midway = Midway()
ball = Ball()
score = Score()
screen.update()

# key bydings
screen.listen()
screen.onkey(fun=right_paddle.Up, key="Up")
screen.onkey(fun=right_paddle.Down, key="Down")
screen.onkey(fun=left_paddle.Up, key="w")
screen.onkey(fun=left_paddle.Down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(.05)
    ball.movement()

    if ball.ycor() >= 240 or ball.ycor() <= -240:
        ball.bounce()

    if (ball.xcor() >= 330 and ball.distance(right_paddle) < 60) or (ball.xcor() <= -334 and ball.distance(left_paddle) < 60):
        ball.paddle_colision()

    if ball.xcor() >= 375: 
        score.left_score()
        ball.right_lose()

    if ball.xcor() <= -375:
        score.right_score()
        ball.left_lose()



    screen.update()



screen.exitonclick()