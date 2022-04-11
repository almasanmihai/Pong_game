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
    ball_position = [int(ball.xcor()), int(ball.ycor())]
    l_pad_position = []
    r_pad_position = []
    for i in range(9):
        lpos = [l_pad.xcor() + 20, l_pad.ycor() - 40 + 10 * i]
        l_pad_position.append(lpos)
        rpos = [r_pad.xcor() -20, r_pad.ycor() - 40 + 10 * i]
        r_pad_position.append(rpos)

    if ball_position in l_pad_position or ball_position in r_pad_position:
        ball.bounce_pad()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_side()

    if ball.xcor() > 360:
        ball.reset_pos()
        score.l_score_up()

    if ball.xcor() < -360:
        ball.reset_pos()
        score.r_score_up()

    if score.game_over():
        is_on = False

screen.exitonclick()
