from turtle import Turtle, Screen
from Paddle import GamePaddle
from GameUI import GameUI
from GameScore import GameScore
from Ball import Ball
import time

screen = Screen()
screen.setup(1000, 740)
screen.screensize(800, 600)
screen.bgcolor("Black")
screen.tracer(0)

drawing_arena = GameUI()
drawing_arena.drawing_arena()
# 1 for player 1 (right) 2 for player 2 (left)
player_score_1 = GameScore(1)
player_score_2 = GameScore(2)

r_paddle = GamePaddle(1)
l_paddle = GamePaddle(-1)

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.002)
    screen.update()
    ball.move()
    if ball.ycor() >= 320 or ball.ycor() <= -320:
        ball.bounce_y()
    if ball.distance(r_paddle) <= 54 and ball.xcor() >= 390 or ball.distance(l_paddle) <= 54 and ball.xcor() <= -390:
        ball.bounce_x()
    if ball.xcor() >= 420:
        player_score_2.update_score()
        ball.restart_game()
    if ball.xcor() <= -420:
        player_score_1.update_score()
        ball.restart_game()






#####
screen.exitonclick()