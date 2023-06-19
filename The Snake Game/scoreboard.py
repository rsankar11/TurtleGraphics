from turtle import Turtle

FONT = ('Courier', 20, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self, height = 600):
        super().__init__()
        self.__score = 0
        with open('The Snake Game/data.txt', mode='r') as file:
            self.__highScore = int(file.read())
        self.__personalBest = 0
        self.hideturtle()
        self.penup()
        self.goto(0, height//2-35)
        self.color("white")
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.__score}  PB: {self.__personalBest}  High Score: {self.__highScore}", align=ALIGNMENT, font=(FONT))
    
    def restart(self):
        if self.__score > self.__highScore:
            self.__highScore = self.__score
            self.__personalBest = self.__score
            with open('The Snake Game/data.txt', mode='w') as file:
                file.write(str(self.__highScore))
        elif self.__score > self.__personalBest:
            self.__personalBest = self.__score
        self.__score = 0
        self.write_scoreboard()

    def increase_score(self):
        self.__score += 1
        self.write_scoreboard()