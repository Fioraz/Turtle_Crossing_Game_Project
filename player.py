from turtle import Turtle

STARTING_POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.speed("fastest")
        self.shapesize(1, 1)
        self.color("black")
        self.reset()

    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset(self):
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()
