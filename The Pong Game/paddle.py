from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, home, game_height):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.left(90)
        self.shapesize(stretch_len=5)
        self.color("white")
        self.goto(home)
        self.__game_height = game_height
    
    def up(self):
        if self.ycor() <= self.__game_height//2-50:
            self.forward(20)

    def down(self):
        if self.ycor() >= -self.__game_height//2+50:
            self.backward(20)
