"""
CS241 - Bullet Class for Skeet
Written by Nolan Meacham

This class inherits the data from the flying objects class. It is used to create a bullet and is called when the user
playing the game clicks the mouse to fire the rifle.

"""

# Import statements.
# Math is used to calculate the velocity of the bullet.
import arcade
import math
from globals import *
from flying_objects_class import FlyingObjects


class Bullet(FlyingObjects):
    """
    Inherits data from flying objects, using the super() command
    Defines the bullet radius using the global declaration

    """

    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS

    def draw(self):
        """
        Draws each bullet as a filled in circle

        """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def fire(self, angle):
        """
        The cos and sin math functions are used here for the bullet velocity. It is dependent on the (x, y) of
        the mouse pointer when the bullet is created which becomes the angel used from the parameter.
        :param angle:

        """
        self.velocity.dx = (math.cos(math.radians(angle)) * BULLET_SPEED)
        self.velocity.dy = (math.sin(math.radians(angle)) * BULLET_SPEED)
