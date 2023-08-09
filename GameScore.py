from turtle import Turtle, Screen


class GameScore(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.player_number = player_number
        self.hideturtle()
        self.color("Yellow")
        self.penup()
        self.speed("fastest")
        self.current_score = 0
        self.go_to_proper_position()
        self.print_game_score()

    def go_to_proper_position(self):
        if self.player_number == 1:
            self.goto(200, 335)
        else:
            self.goto(-200, 335)

    def print_game_score(self):
        self.clear()
        self.go_to_proper_position()
        self.write(f"Current score: {self.current_score}", True, "Center", ("Arial", 10, "normal"))

    def update_score(self):
        self.current_score += 1
        self.print_game_score()

