#####################################
# ball.py
# by Britte Genzlinger
####################################
import random
import turtle
import math

class Ball():
    """ A colored circle of random size and random shade of blue
    that moves in a random direction and random speed around the screen.
    When it encounters the edge of the screen,
    it "bounces" off.
    """
    def __init__(self):
        """ Creates a Ball object using Turtle
        """
        self.x = random.random()
        self.y = random.random()
        self.xVel = (random.random()/100)-.005
        self.yVel = (random.random()/100)-.005
        self.size = random.random()*2
        self.bTurtle = turtle.Turtle()
        self.bTurtle.shape("circle")
        self.setColor()
        self.setSize(self.size)

    def setPos(self, x, y):
        """ Moves the ball to a new location
        """
        self.bTurtle.goto(x,y)

    def setColor(self):
        """ Sets the color of the ball to a random shade of green.
        """
        r = 0
        g = .8
        b = 0
        myColor = (r,g,b)
        self.bTurtle.color(myColor)

    def setSize(self,size):
        """Changes size of ball

        Arg:
        size: floating point number to determine the size of the ball
        """
        self.bTurtle.resizemode("user")
        self.bTurtle.turtlesize(size)

    def update(self):
        """Checks whether the ball has hit a wall.
        If the ball has hit a wall, it changes the direction of movement
        to immitate a "bounce"
        """
        if self.x < 0 or self.x > 1:
            self.xVel = self.xVel*-1
        if self.y < 0 or self.y > 1:
            self.yVel = self.yVel*-1

    def move(self):
        """Moves the ball slightly along its current path
        """
        self.bTurtle.up()
        self.x += self.xVel
        self.y += self.yVel
        self.setPos(self.x,self.y)


class WarpBall(Ball):
    """ WarpBall extends the Ball class.
    A WarpBall is the same as a Ball,
    but instead of bouncing off the wall,
    it reappears on the other side of the screen.
    """
    def __init__(self):
        super().__init__()

    def update(self):
        """Checks whether the ball has hit a wall.
        If the ball has hit a wall, it "warps" the ball
        onto the opposite side of the screen
        """
        if self.x > 1:
            self.x = 0
        if self.y > 1:
            self.y = 0

# ----------- 💻 PART 1️⃣: WRITE YOUR CODE HERE ⬇️ -----------
  




class BreathingBall(Ball):
    """ BreathingBall extends the Ball class.
    A BreathingBall is the same as a Ball,
    but it grows and shrinks as it moves.
    """
    def __init__(self):
        """This constructor calls the constructor of the parent class,
        and adds a counter variable.
        """
        super().__init__()
        self.step = random.randint(0,120)
        
    def update(self):
        """Calls the parent method and also changes the size of the ball
        """
        super().update()
        self.step += 1
        newRadius = math.sin(self.step/20)*(3/2)+1.5
        self.setSize(newRadius)

# ----------- 💻 PART 2️⃣: WRITE THE CODE HERE ⬇️ -----------
 