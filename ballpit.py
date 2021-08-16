##########################################
# ballpit.py
# by Britte Genzlinger
###########################################
import turtle
from ball import *

def ball_pit():
    """ Initializes the ball pit with each type of ball.
    """
    turtleWorld = turtle.Turtle()
    turtle.setworldcoordinates(0, 0, 1, 1)
    turtle.tracer(50)
    turtleWorld.hideturtle()

    ballList = [Ball(),BreathingBall(),WarpBall()]
    
    while True:
        for b in ballList:
            b.update()
            b.move()


if __name__ == "__main__":
    ball_pit()