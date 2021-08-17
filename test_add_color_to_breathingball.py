##########################################
# test_add_color_to_breathingball.py
# by Emma Brown and Britte Genzlinger
###########################################

from setup_ballpit_canvas import setup_ballpit_canvas
from ball import BreathingBall

def test_add_color_to_breathingball():
    """ Initializes a Turtle canvas with a single BreathingBall.
    """
    breathing_ball = BreathingBall()
    
    while True:
        breathing_ball.update()
        breathing_ball.move()


if __name__ == "__main__":
    test_add_color_to_breathingball()
    ball_pit()



