from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_side(self):
        self.ymove *= -1

    def bounce_pad(self):
        self.xmove *= -1
        self.move_speed *= 0.9


    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_pad()
        self.move_speed = 0.1
