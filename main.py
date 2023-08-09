import time
from turtle import Screen
from Player import Player
from Car_manager import CarManager
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 700)
screen.screensize(6000, 6000)
screen.bgcolor("white")
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

screen.update()

game_is_on = True
time_sleep = 0.1

while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    car_manager.move_cars()
    for current_car in car_manager.cars:
        if player.distance(current_car) <=15:
            game_is_on = False
            score.print_you_lost()
    if player.ycor() >= 280:
        score.print_score()
        player.goto(x=0, y=-280)
        time_sleep *= 0.95




screen.exitonclick()