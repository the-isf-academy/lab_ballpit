##########################################
# ballpit.py
# Teachers: Emma Brown and Britte Genzlinger
# Student: YOUR NAME GOES HERE
############################################

from setup_ballpit_canvas import setup_ballpit_canvas
from ball import *

def ball_pit():
    """ Initializes the ball pit with each type of ball.
    """
    ballList = [Ball(),WarpBall(),BreathingBall()]
    
    while True:
        for i in range(len(ballList)):
            ballList[i].update()
            ballList[i].move()


if __name__ == "__main__":
    setup_ballpit_canvas()
    ball_pit()



