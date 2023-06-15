import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Turtle Crossing Game")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(player.move, "Up")
    time.sleep(0.001)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect arrival of turtle
    if player.ycor() > 270:
        player.reset()
        car_manager.speed_up()
        scoreboard.new_level()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()





