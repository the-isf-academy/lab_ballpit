##########################################
# ballpit.py
# by Britte Genzlinger
###########################################
import turtle
from ball import *

def ball_pit():
    turtleWorld = turtle.Turtle()
    turtle.setworldcoordinates(0, 0, 1, 1)
    turtle.tracer(50)
    turtleWorld.hideturtle()

    ballList = []

    for i in range(10):
        ballList.append(Ball())
        ballList.append(BreathingBall())
        ballList.append(WarpBall())
    
    while True:
        for i in range(len(ballList)-1):
            ballList[i].update()
            ballList[i].move()
            ballList[i].setColor()


if __name__ == "__main__":
    ball_pit()