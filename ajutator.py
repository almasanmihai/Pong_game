
from turtle import Screen
from turtle import Turtle

class PlayerPad(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 5, 1)
        self.goto(-890, 0)
        self.setheading(90)

    def create_pad(self):
       pass

    def move(self):
        self.forward(50)

    def up(self):
        y = self.ycor() + 20
        self.sety(y)

    def down(self):
        y = self.ycor() - 20
        self.sety(y)



screen = Screen()
screen.bgcolor("black")
screen.setup(width=1800, height=1000)
screen.title("My Pong game")
# screen.tracer(0)

pad = PlayerPad()

screen.listen()
screen.onkey(pad.up(), "w")
screen.onkey(pad.down(), "s")

screen.mainloop()

# is_on = True
# while is_on:
#     # screen.update()
#
#     # pad.move()




screen.exitonclick()
