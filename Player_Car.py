from turtle import Turtle

Starting_Positon = (0, -280)
Move_Distance = 10
Finish_Line_y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(Move_Distance)

    def go_down(self):
        self.backward(Move_Distance)

    def finish_game(self):
        if self.ycor() > Finish_Line_y:
            return True
        return False

    def go_to_start(self):
        self.goto(Starting_Positon)
