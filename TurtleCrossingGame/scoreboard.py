from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.__level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-190,250)
        self.next_level()

    def next_level(self):
        self.__level += 1
        self.clear()
        self.write(f"Level: {self.__level}", align=ALIGN, font=FONT)
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGN, font=FONT)
