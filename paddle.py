from turtle import Turtle
MOVE_PADDLE = 20

# CREATING A PADDLE

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.width(20)
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1, 1)
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        self.sety(y + MOVE_PADDLE)

    # MOVING PADDLE DOWN
    def move_down(self):
        y = self.ycor()
        self.sety(y - MOVE_PADDLE)

