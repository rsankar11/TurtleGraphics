from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH, HEIGHT = 800, 600
GAME_SPEED = 0.06             #The lower the number the faster the game speed

screen = Screen()
screen.setup(width = WIDTH, height = HEIGHT)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

r_paddle = Paddle((350,0), game_height = HEIGHT)
l_paddle = Paddle((-350,0), game_height = HEIGHT)
ball = Ball(GAME_SPEED)
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.get_game_speed())
    ball.move()
    ball.detect_wall(HEIGHT)
    ball.detect_paddle(r_paddle, Right=True)
    ball.detect_paddle(l_paddle, Left=True)
    ball.detect_out_of_bounds(WIDTH, scoreboard)
    if(scoreboard.game_over()):
        game_on = False

screen.exitonclick()