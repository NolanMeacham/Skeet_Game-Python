"""
CS241 - Standard Target for Skeet
Written by Nolan Meacham

The standard target is a "Flying Object" and inherits the data from Target class, which gets data from the
Flying Objects class.

The standard target is a solid color filled circle and takes one hit to remove and adds 1 point when destroyed.
It will always start from the left side of the screen, with a random velocity in the x and y direction. The spawn area
for the y value is randomly selected between the top half of the screen.

"""

import random
from globals import *
from target_class import Target


class StandardTarget(Target):
    """
    Standard Target
    Inherit data from Target class using super()
    Redefine variables for x and y
    Define the radius using the global declaration from the globals file
    Define the velocity, as a random number between the ranges listed below.

    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_HEIGHT)
        self.radius = STD_TARGET_RADIUS
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-3, 2)

    def draw(self):
        """
        Draws each standard target

        """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, STD_TARGET_COLOR)

    def hit(self):
        """
        This method is used simply to add a point to the users score using the return
         and set the alive boolean to false.

        """
        self.alive = False
        return 1
