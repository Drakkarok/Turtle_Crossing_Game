from turtle import Turtle


class GamePaddle(Turtle):

    def __init__(self, right_or_left):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('White')
        self.goto(x=right_or_left * 410, y=0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() >= 280:
            self.goto(self.xcor(), 280)
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() <= -280:
            self.goto(self.xcor(), -280)
        else:
            self.goto(self.xcor(), self.ycor() - 20)
