from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
# CREATE SCREEN AND OBJECTS
screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()



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
    time.sleep(0.1)

    ball.move_ball()
    screen.update()

    # DETECT COLLISION WITH WALLS
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

#   DETECT COLLISION WITH A PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.deflect()



screen.exitonclick()
