from scoreboard import Scoreboard
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

FONT = ("Courier", 80, "normal")
CENTER = "center"

#create screen 1000x800 pixels
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("midnight blue")
screen.title("PyPong")
screen.tracer(0)

#create scoreboard
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.accelerate)
    screen.update()
    ball.move()
    #collision if ball hits upper or lower edge of screen
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    #collision if ball hits paddle
    if ball.distance(right_paddle) < 25 and ball.xcor() > 380 or ball.distance(left_paddle) < 25 and ball.xcor() < -380:
        ball.bounce_x()
    #detect right paddle missing the ball
    if ball.xcor() > 480:
        scoreboard.left_point()
        ball.position_reset()
        scoreboard.update_scoreboard()
    #detect right paddle missing the ball
    if ball.xcor() < -480:
        scoreboard.right_point()
        ball.position_reset()
        scoreboard.update_scoreboard()
#game end condition
    if scoreboard.left_score == 10:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.goto(0, -200)
        scoreboard.write("Left Player WINS", align=CENTER, font= FONT)

    elif scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.goto(0, -200)
        scoreboard.write("Right Player WINS", align=CENTER, font= FONT)


screen.exitonclick()
