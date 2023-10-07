from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import time
MOVE_DISTANCE=20
screen=Screen()
screen.bgcolor("Black")
screen.setup(height=600,width=800)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
l_score=Scoreboard((-200,270))
r_score=Scoreboard((200,270))
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
screen.onkey(ball.move,"m")

game_is_on=True
while game_is_on:
    time.sleep(ball.Move_speed)
    screen.update()
    ball.move()
    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        #collosion occure
        ball.bounce()
    #dtect collision with  paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.peddle_bounce()
    #detect when paddle miss the ball
    if ball.xcor() >380:
        ball.reset_position()
        l_score.increase_score()
    if ball.xcor() < -380:
        ball.reset_position()
        r_score.increase_score()
    if l_score.score == 10 or r_score == 10:
        l_score.game_over()
        game_is_on=False


screen.exitonclick()
