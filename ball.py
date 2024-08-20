import random
import math
from turtle import *

class Ball():
    # A colored circle of random size and random shade of green
    # that moves in a random direction and random speed around the screen.
    # When it encounters the edge of the screen,
    # it "bounces" off.

    def __init__(self):
        # Creates a Ball object using Turtle

        self.x = random.random()
        self.y = random.random()
        
        self.x_vel = random.uniform(.0001,.001)
        self.y_vel = random.uniform(.0001,.001)
        
        self.size = random.randint(1,10)

        self.turtle = Turtle()
        self.turtle.shape("circle")

        self.set_color()
        self.set_size(self.size)

    def set_position(self, x, y):
        # Moves the ball to a new location
        
        self.turtle.goto(x,y)

    def set_size(self,size):
        # Changes size of ball

        self.turtle.resizemode("user")
        self.turtle.turtlesize(size)

    def update(self):
        # Checks whether the ball has hit a wall.
        # If the ball has hit a wall, it changes the direction of movement
        # to immitate a "bounce"

        if self.x < 0 or self.x > 1:
            self.x_vel = self.x_vel*-1
        if self.y < 0 or self.y > 1:
            self.y_vel = self.y_vel*-1

    def move(self):
        # Moves the ball slightly along its current path
       

        self.turtle.up()
        self.x += self.x_vel
        self.y += self.y_vel
        self.set_position(self.x,self.y)

    def set_color(self):
        # Sets the color of the ball to a shade of green.

        r = 0
        g = .8
        b = 0

        my_color = (r,g,b)
        self.turtle.color(my_color)


# ----------- 💻 PASTE CODE HERE ⬇️ -----------
