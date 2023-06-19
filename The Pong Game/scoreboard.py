from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80,"normal")
SCORE_TO_WIN = 5

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.update()
        
    def l_point(self):
        self.__l_score += 1
        self.update()
    
    def r_point(self):
        self.__r_score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.__l_score, align=ALIGN, font=FONT)
        self.goto(100, 190)
        self.write(self.__r_score, align=ALIGN, font=FONT)
    
    def game_over(self):
        if self.__l_score >= SCORE_TO_WIN or self.__r_score >= SCORE_TO_WIN:
            self.goto(0,-60)
            self.write("GAME OVER", align=ALIGN, font=FONT)
            return True