##########################################
# test_add_color_to_warpball.py
# by Emma Brown and Britte Genzlinger
###########################################

from setup_ballpit_canvas import setup_ballpit_canvas
from ball import WarpBall

def test_add_color_to_warpball():
    """ Initializes a Turtle canvas with a single WarpBall.
    """
    warp_ball = WarpBall()
    
    while True:
        warp_ball.update()
        warp_ball.move()


if __name__ == "__main__":
    setup_ballpit_canvas()
    test_add_color_to_warpball()



