import time
from turtle import Screen, Turtle
from player_pad import PlayerPad

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong game")
screen.tracer(0)

pad1 = PlayerPad()
pad2 = PlayerPad()
pad2.goto(350, 0)

screen.listen()
screen.onkey(pad1.up, "w")
screen.onkey(pad1.down, "s")
screen.onkey(pad2.up, "Up")
screen.onkey(pad2.down, "Down")



is_on = True
while is_on:
    screen.update()
    time.sleep(0.2)
    # pad.move()




screen.exitonclick()