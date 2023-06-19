import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUM_CARS = 25
COUNT_MOD = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
c_manager = CarManager(NUM_CARS)
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player.moveUp, "Up")
screen.onkeypress(player.moveLeft, "Left")
screen.onkeypress(player.moveRight, "Right")

game_is_on = True
counter = 1
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Checks if player made it to end of level
    if player.next_level_check():
        scoreboard.next_level()
        c_manager.next_level()

    # Populates first "NUM_CARS" every "COUNT_MOD" runs
    if counter%COUNT_MOD == 0 and counter <= NUM_CARS*COUNT_MOD:
        c_manager.generate_car()
        c_manager.delete_cars()
    
    # Ffter first "NUM_CARS" populated, creates cars automaticaly with limit
    # of "NUM_CARS" cars on screen at a time
    elif counter > NUM_CARS*COUNT_MOD:
        c_manager.generate_car()
        c_manager.delete_cars()

    c_manager.move()

    # Checks if any cars hit player
    if (c_manager.hit(player)):
        scoreboard.game_over()
        screen.update()
        game_is_on = False

    counter+=1

screen.exitonclick()
