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


    # def move(self):
    #     self.forward(50)

    def up(self):
        y = self.ycor() + 20
        self.sety(y)

    def down(self):
        y = self.ycor() - 20
        self.sety(y)



