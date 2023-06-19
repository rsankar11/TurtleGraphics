from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP, LEFT, RIGHT = 90, 180, 0


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def moveUp(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)
    
    def moveLeft(self):
        self.setheading(LEFT)
        self.forward(MOVE_DISTANCE)
    
    def moveRight(self):
        self.setheading(RIGHT)
        self.forward(MOVE_DISTANCE)
    
    def next_level_check(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.setheading(UP)
            return True

