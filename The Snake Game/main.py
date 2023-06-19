from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.07             #The lower the number the faster the game speed
WIDTH, HEIGHT = 600, 600

# screen set-up
screen = Screen()
screen.setup(width = WIDTH, height = HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# class intialization
snake = Snake()
food = Food()
scoreboard = Scoreboard(HEIGHT)

# keybinding
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game mechanics
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    if snake.impact(food):
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.out_of_bounds(height = HEIGHT, width = WIDTH):
        screen.update()
        scoreboard.restart()
        snake.restart()
    
    if snake.hit_tail():
        scoreboard.restart()
        snake.restart()

screen.exitonclick()