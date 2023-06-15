from turtle import Turtle
import random

car_colors = ["blue", "red", "green", "pink", "black", "yellow", "orange", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_speed = MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1 or random_chance == 2:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(car_colors))
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.showturtle()
            car.backward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT


