from turtle import Turtle, Screen


class GameUI(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(1)
        self.color("white")
        self.penup()

    def drawing_arena(self):
        self.goto(x=-400,y=330)
        self.pendown()
        self.setheading(0)
        self.forward(800)
        self.setheading(270)
        self.penup()
        self.interrupt_line(660)
        self.setheading(180)
        self.pendown()
        self.forward(800)
        self.setheading(90)
        self.interrupt_line(660)
        self.penup()
        self.goto(x=0, y=-330)
        self.setheading(90)
        self.interrupt_line(700)

    def interrupt_line(self, distance):
        x = True
        travelled_distance = 0
        while x:
            travelled_distance += 20
            self.forward(8)
            self.pendown()
            self.forward(4)
            self.penup()
            self.forward(8)
            if travelled_distance >= distance:
                x = False

