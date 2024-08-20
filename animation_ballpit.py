from turtle import *
from ball import Ball

## sets up the Turtle canvas
setworldcoordinates(0, 0, 1, 1)
tracer(30)
bgcolor((1,1,1))


## creates multiples instances of Ball() 
ball_list = []
for i in range(3):
    ball_list.append(Ball())


## animates the ballpit 
while True:
    for ball in ball_list:
        ball.update()
        ball.move()



