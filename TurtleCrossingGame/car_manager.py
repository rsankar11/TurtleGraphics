import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    
    def __init__(self, num_cars):
        self.__cars = []
        self.__move_distance = STARTING_MOVE_DISTANCE
        self.__num_cars = num_cars

    def generate_car(self):
        if len(self.__cars) < self.__num_cars:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            x = 320
            y = random.randint(-250,250)
            new_car.goto(x,y)
            new_car.setheading(180)
            self.__cars.append(new_car)

    def move(self):
        for car in self.__cars:
            car.forward(self.__move_distance)
    
    def delete_cars(self):
        for car in self.__cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.__cars.remove(car)
    
    def next_level(self):
        self.__move_distance += MOVE_INCREMENT
    
    def hit(self, ttl):
        for car in self.__cars:
            if car.distance(ttl)<=21:
                return True
            elif car.distance(ttl)<=30 and (ttl.xcor() > car.xcor()+20 or ttl.xcor() < car.xcor()-20):
                return True
        return False
