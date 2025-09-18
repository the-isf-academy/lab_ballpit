from turtle import *
from ball import Ball, BreathingBall, WarpBall
from datetime import datetime

## sets up the Turtle canvas
setworldcoordinates(0, 0, 1, 1)
tracer(30)
bgcolor((1,1,1))


## creates multiples instances of Ball() 
ball_list = []
for i in range(3):
    ball_list.append(Ball())

for i in range(10):
    ball_list.append(BreathingBall())

for i in range(5):
    ball_list.append(WarpBall())


## animates the ballpit 
while True:
    for ball in ball_list:
        ball.update()
        ball.move()

        # change colors randomly after every 100 microseconds
        # if (datetime.now().microsecond % 100 == 0):
            # ball.random_color()



