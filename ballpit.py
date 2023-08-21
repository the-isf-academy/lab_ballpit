# ballpit.py

from setup_ballpit_canvas import setup_ballpit_canvas
from ball import Ball

def ball_pit():
    """ Initializes the ball pit"""

    ballList = []
    for i in range(3):
        ballList.append(Ball())

    
    while True:
        for ball in ballList:
            ball.update()
            ball.move()



setup_ballpit_canvas()
ball_pit()



