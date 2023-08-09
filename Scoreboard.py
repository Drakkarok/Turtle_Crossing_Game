from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(x=-225, y=300)
        self.score = -1
        self.print_score()

    def print_score(self):
        self.clear()
        self.score += 1
        self.write(f"Your current score is {self.score}", False, 'center', ('Arial', 11, 'normal'))

    def print_you_lost(self):
        self.goto(x=0, y=280)
        self.color("Red")
        self.write("You lost :(", False, 'center', ('Arial', 16, 'normal'))




