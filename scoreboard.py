from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.goto(-100, 200)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score_display()
    def r_score_up(self):
        self.clear()
        self.score_r += 1
        self.score_display()
    def l_score_up(self):
        self.clear()
        self.score_l += 1
        self.score_display()
    def score_display(self):
        self.write(f"{self.score_l} : {self.score_r}", font=("Courier", 50, "bold"))
    def game_over(self):
        if self.score_l == 5 or self.score_r == 5:
            return True