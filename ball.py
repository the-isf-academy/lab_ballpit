import random
import math
from turtle import *
import time

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
        # self.turtle.shape("circle")
        self.turtle.shape("turtle")

        self.set_color()
        self.set_size(self.size)

    def set_position(self, x, y):
        # Moves the ball to a new location
        
        self.turtle.goto(x,y)

    def set_size(self,size):
        # Changes size of ball

        self.turtle.resizemode("user")
        self.turtle.turtlesize(size)

        # for outline
        # self.turtle.pencolor("black")

        # turtlesize parameters: stretch_wid, stretch_len, outline
        # self.turtle.turtlesize(size, size, size/10)

    def update(self):
        # Checks whether the ball has hit a wall.
        # If the ball has hit a wall, it changes the direction of movement
        # to immitate a "bounce"

        if self.x <= 0 or self.x > 1:
            self.x_vel = self.x_vel*-1
        if self.y < 0 or self.y > 1:
            self.y_vel = self.y_vel*-1

        # change orientation of the turtle
        self.turtle.tilt(random.randint(10,20))

    def move(self):
        # Moves the ball slightly along its current path

        self.turtle.up()
        self.x += self.x_vel
        self.y += self.y_vel
        self.set_position(self.x,self.y)

    def set_color(self):
        # Sets the color of the ball to a shade of green.

        r = 0
        g = random.uniform(0,0.8)
        b = 0

        my_color = (r,g,b)
        self.turtle.color(my_color)
    
    def random_color(self):
        r = random.uniform(0,0.8)
        g = random.uniform(0,0.8)
        b = random.uniform(0,0.8)

        my_color = (r,g,b)
        self.turtle.color(my_color)


# ----------- 💻 PASTE CODE HERE ⬇️ -----------
class BreathingBall(Ball):
    # BreathingBall extends the Ball class.
    # A BreathingBall is the same as a Ball,
    # but it grows and shrinks as it moves.

    def __init__(self):
        # This constructor calls the constructor of the parent class,
        # and adds a step variable.
        
        super().__init__()
        
        self.step = random.randint(0,120)
        
    def update(self):
        # Calls the parent method and also changes the size of the ball
        
        super().update()

        self.step += 1
        new_radius = math.sin(self.step/20)*(3/2)+1.5
        self.set_size(new_radius)
    
    def set_color(self):
        # Sets the color of the ball to a shade of red
        r = random.uniform(0,0.8)
        g = 0
        b = 0

        my_color = (r,g,b)
        self.turtle.color(my_color)


class WarpBall(Ball):
    # WarpBall extends the Ball class.
    # A WarpBall is the same as a Ball,
    # but instead of bouncing off the wall,
    # it reappears on the other side of the screen.

    def __init__(self):
        super().__init__()

    def update(self):
        # Checks whether the ball has hit a wall.
        # If the ball has hit a wall, it "warps" the ball
        # onto the opposite side of the screen        

        if self.x > 1:
            self.x = 0
        if self.y > 1:
            self.y = 0
    
    def set_color(self):
        # Sets the color of the ball to a shade of blue
        r = 0
        g = 0
        b = random.uniform(0,0.8)

        my_color = (r,g,b)
        self.turtle.color(my_color)
