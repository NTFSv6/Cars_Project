from turtle import Turtle

Font = ("Courier", 24, 'normal')

class scoreboard(Turtle):

    def __init__(self):
        super(scoreboard, self).__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-285, 260)
        self.update_scorebord()

    def update_scorebord(self):
        self.clear()
        self.color("white")
        self.write(f"Level: {self.level}", align='left', font=Font)

    def increase_level(self):
        self.level += 1
        self.update_scorebord()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align = "center", font=Font)
