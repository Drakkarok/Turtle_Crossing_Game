from turtle import Turtle
STARTING_POSITION = (0, -282)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color = "green"
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_len=0.7, stretch_wid=0.8)

    def move(self):
        self.forward(10)
