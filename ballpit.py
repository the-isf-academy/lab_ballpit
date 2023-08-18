# ballpit.py

from setup_ballpit_canvas import setup_ballpit_canvas
from ball import Ball, BreathingBall

def ball_pit():
    """ Initializes the ball pit with each type of ball.
    """

    ballList = []
    for i in range(10):
        ballList.append(Ball())
        ballList.append(BreathingBall())

    
    while True:
        for ball in ballList:
            ball.update()
            ball.move()



setup_ballpit_canvas()
ball_pit()



