from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.color("black")
        self.write(f"Level: {self.level}", align="left", font=("Arial", 15, "normal"))

    def new_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
