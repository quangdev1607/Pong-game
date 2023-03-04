from turtle import Turtle, Screen

screen = Screen()
CURRENT_Y_UP = 0
CURRENT_Y_DOWN = 0


class GameScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.go_up()
        self.go_down()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 220)
        self.write(f"{self.score_left}", align="center", font=("Arial", 50, "normal"))
        self.goto(200, 220)
        self.write(f"{self.score_right}", align="center", font=("Arial", 50, "normal"))

    def go_up(self):
        global CURRENT_Y_UP
        for _ in range(20):
            cube = Turtle("square")
            cube.penup()
            cube.color("white")
            cube.shapesize(0.5, 0.5)
            cube.goto(0, CURRENT_Y_UP)
            CURRENT_Y_UP += 20

    def go_down(self):
        global CURRENT_Y_DOWN
        for _ in range(20):
            cube = Turtle("square")
            cube.penup()
            cube.color("white")
            cube.shapesize(0.5, 0.5)
            cube.goto(0, CURRENT_Y_DOWN)
            CURRENT_Y_DOWN -= 20

    def increase_left_score(self):
        self.score_left += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.score_right += 1
        self.update_scoreboard()
