from turtle import Turtle


class PlayerPad(Turtle):
    def __init__(self):
        super().__init__()
        self.create_pad()

    def create_pad(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(-350, 0)

    def up(self):
        if self.ycor() == 280:
            y = self.ycor()
        else:
            y = self.ycor() + 20
        self.sety(y)

    def down(self):
        if self.ycor() == -280:
            y = self.ycor()
        else:
            y = self.ycor() - 20
        self.sety(y)
