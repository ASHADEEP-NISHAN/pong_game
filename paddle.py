from turtle import Turtle
STARTING_POSSITION=[(350,0),(350,-20),(350,-40),(350,-60),(350,-80)]
MOVE_DISTANCE=20
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("White")
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)



