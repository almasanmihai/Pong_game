import time
from turtle import Screen
from player_pad import PlayerPad
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong game")
screen.tracer(0)

l_pad = PlayerPad()
r_pad = PlayerPad()
r_pad.goto(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_pad.up, "w")
screen.onkeypress(l_pad.down, "s")
screen.onkeypress(r_pad.up, "Up")
screen.onkeypress(r_pad.down, "Down")

is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_side()

    if ball.xcor() > 350:
        ball.reset_pos()
        score.l_score_up()

    if ball.xcor() < -350:
        ball.reset_pos()
        score.r_score_up()

    if ball.distance(r_pad) < 50 and ball.xcor() > 330:
        ball.bounce_pad()

    if ball.distance(l_pad) < 50 and ball.xcor() < -330:
        ball.bounce_pad()
    if score.game_over():
        is_on = False

screen.exitonclick()