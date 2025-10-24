from turtle import Screen, Turtle
MOVE_PADDLE = 20

# CREATE SCREEN AND LISTEN TO EVENTS
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()


# MOVING PADDLE UP
def move_up():
    y = paddle.ycor()
    paddle.sety(y + MOVE_PADDLE)
# MOVING PADDLE DOWN
def move_down():
    y = paddle.ycor()
    paddle.sety(y - MOVE_PADDLE)

# CREATING A PADDLE
paddle = Turtle()
paddle.width(20)
paddle.penup()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(5, 1, 1)
paddle.goto(350, 0)

# MOVE EVENTS
screen.onkeypress(move_up,'Up')
screen.onkeypress(move_down,'Down')




screen.exitonclick()