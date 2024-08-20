import turtle
from ball import Ball

## sets up the Turtle for animation. 
turtle.setworldcoordinates(0, 0, 1, 1)
turtle.tracer(30)


## creates multiples instances of Ball() 
ballList = []
for i in range(3):
    ballList.append(Ball())


## animates the ballpit 
while True:
    for ball in ballList:
        ball.update()
        ball.move()



