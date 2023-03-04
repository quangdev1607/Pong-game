from turtle import Screen
from game_screen import GameScreen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Pong")
screen.tracer(0)

game_screen = GameScreen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
game_is_on = True
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed -= 0.01
        print(f"Current speed: {ball.move_speed}")

    # Right miss
    if ball.xcor() > 380:
        ball.refresh()
        ball.move_speed = 0.1
        game_screen.increase_left_score()
    # Left miss
    if ball.xcor() < -380:
        ball.refresh()
        ball.move_speed = 0.1
        game_screen.increase_right_score()
screen.exitonclick()
