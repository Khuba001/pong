from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# CREATE SCREEN AND OBJECTS
screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)





# MOVE EVENTS
screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')


screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')
# GAME STATUS AND MANUAL SCREEN UPDATE
game_on = True

while game_on:
    time.sleep(ball.ball_speed)

    ball.move_ball()
    screen.update()

    # DETECT COLLISION WITH WALLS
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#   DETECT COLLISION WITH A PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.deflect()

    # DETECT PLAYER MISSING A BALL
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if  ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
