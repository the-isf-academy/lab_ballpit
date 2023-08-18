# Setup for Ballpit Canvas

import turtle

def setup_ballpit_canvas():
    """ Sets up the Turtle canvas specifications for the ballpit. 
    """
    turtleWorld = turtle.Turtle()
    turtle.setworldcoordinates(0, 0, 1, 1)
    turtle.tracer(50)
    turtleWorld.hideturtle()