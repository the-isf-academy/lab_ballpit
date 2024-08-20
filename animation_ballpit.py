from turtle import *
from ball import Ball

## sets up the Turtle canvas
setworldcoordinates(0, 0, 1, 1)
tracer(30)
bgcolor((1,1,1))


## creates multiples instances of Ball() 
ballList = []
for i in range(3):
    ballList.append(Ball())


## animates the ballpit 
while True:
    for ball in ballList:
        ball.update()
        ball.move()



