from turtle import Turtle

STARTING_X, STARTING_Y = 0,0
STARTING_LEN = 3 
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:

    def __init__(self):
        self.__segments = []
        self.create_snake()
        self.__head = self.__segments[0]
    
    def create_snake(self):
        for i in range(STARTING_LEN):
            x = STARTING_X - (20*i)
            self.add_segment((x,STARTING_Y))
    
    def add_segment(self, position):
        newTtl = Turtle(shape="square")
        newTtl.penup()
        newTtl.goto(position)
        newTtl.color("white")
        self.__segments.append(newTtl)

    def extend(self):
        self.add_segment(self.__segments[-1].position())
    
    def move(self):
        for i in range(len(self.__segments)-1, 0, -1):
            ttl = self.__segments[i]
            new_x = self.__segments[i-1].xcor()
            new_y = self.__segments[i-1].ycor()
            ttl.goto(new_x,new_y)
        self.__head.forward(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)
    
    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)
    
    def impact(self, ttl):
        """
        returns T/F if the snake head has bumped into passed in turtle item
        """
        return self.__head.distance(ttl) < 16

    def out_of_bounds(self, height, width):
        """
        Takes in a input for height and width of game board and then creates
        a boundary. Returns a boolean on "out of bounds" status
        """
        y_boundary = height//2-10
        x_boundary = width//2-10
        return abs(self.__head.xcor()) > x_boundary or abs(self.__head.ycor()) > y_boundary
    
    def hit_tail(self):
        for seg in self.__segments[1:]:
            if self.impact(seg):
                return True
        return False
    
    def restart(self):
        for seg in self.__segments:
            seg.goto(1000,1000)
            seg.hideturtle()
        self.__segments.clear()
        self.create_snake()
        self.__head = self.__segments[0]