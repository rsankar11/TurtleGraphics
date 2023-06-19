import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self, game_speed):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.setheading(45)
        self.penup()
        self.color("white")
        self.__x_move = 10
        self.__y_move = 10
        self.__game_speed = game_speed
        self.__starting_speed = game_speed
        self.restart(goLeft=random.choice([True,False]), goRight=True)
    

    def move(self):
        new_x = self.xcor() + self.__x_move
        new_y = self.ycor() + self.__y_move
        self.goto(new_x, new_y)


    def detect_wall(self, game_height):
        if abs(self.ycor()) > game_height//2-20:
            self.__y_move *= -1

    
    def detect_paddle(self, paddle, Left = False, Right = False):
        if self.distance(paddle) <= 50:
            if Right:
                left_margin = paddle.xcor() - 15
                if self.xcor() >= left_margin:
                    self.__x_move = -(abs(self.__x_move))
                    self.increase_speed()
            elif Left:
                right_margin = paddle.xcor() + 15
                if self.xcor() <= right_margin:
                    self.__x_move = abs(self.__x_move)
                    self.increase_speed()


    def detect_out_of_bounds(self, width, scoreboard):
        if self.xcor() > width//2 - 10:
            scoreboard.l_point()
            self.restart(goLeft = True)
        elif self.xcor() < -width//2:
            scoreboard.r_point()
            self.restart(goRight=True)
    

    def restart(self, goLeft=False, goRight=False):
        self.home()
        if goLeft:
            self.__x_move = -10
        elif goRight:
            self.__x_move = 10
        self.__y_move = random.choice([10,-10])
        self.__game_speed = self.__starting_speed

    
    def increase_speed(self):
        self.__game_speed *= 0.85
        return self.__game_speed
    

    def get_game_speed(self):
        return self.__game_speed