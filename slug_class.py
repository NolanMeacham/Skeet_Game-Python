"""
CS241 - Slug Class for Skeet
Written by Nolan Meacham

The slug class is similar to the bullet class.
The difference is the larger radius and reduced velocity.

"""

import math
from globals import *
from flying_objects_class import FlyingObjects


class Slug(FlyingObjects):
    """
    Inherits data from flying objects, using the super() command
    Defines the slug radius using and increasing the global declaration

    """

    def __init__(self):
        super().__init__()
        self.radius = (BULLET_RADIUS + 7)

    def draw(self):
        """
        Draws each slug as a filled in circle

        """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, arcade.color.DARK_SLATE_GRAY)

    def fire(self, angle):
        """
        The cos and sin math functions are used here for the bullet velocity. It is dependent on the (x, y) of
        the mouse pointer when the bullet is created which becomes the angle used from the parameter.
        :param angle:

        """
        self.velocity.dx = (math.cos(math.radians(angle)) * (BULLET_SPEED-2))
        self.velocity.dy = (math.sin(math.radians(angle)) * (BULLET_SPEED-2))
