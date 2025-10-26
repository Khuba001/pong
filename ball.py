from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        # SPEED OF WHICH THE BALL MOVES
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        # WHEN BALL HITS WALL THE SPEED IS NOW -10 AND THE BALL MOVES DOWN
        # TILL IT HITS BOTTOM WALL AND * -1 MAKE IT POSITIVE AGAIN
        self.y_move *= -1

    def deflect(self):
        # SAME AS BOUNCE BUT WITH THE X COORDINATE
        self.x_move *= -1

