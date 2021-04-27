"""
CS241 - Safe Targets for Skeet
Written by Nolan Meacham

The standard target is a "Flying Object" and inherits the data from Target class, which gets data from the
Flying Objects class.

The safe target is a small square which the user should avoid shooting. The safe target only takes 1 shot to destroy.
If the safe target is shot, the user loses 10 points from their score. It follows the same
spawn pattern as the other targets.
"""

import random
from globals import *
from target_class import Target


class SafeTarget(Target):
    """
    Safe Target
    Inherit data from Target class using super()
    Redefine variables for x and y
    Define the radius using the global declaration from the globals file
    Define the velocity, as a random number between the ranges listed below.

    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_HEIGHT)
        self.radius = TARGET_SAFE_RADIUS
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-2, 3)

    def draw(self):
        """
        Unlike the other targets, the safe target is a filled in square. The width and height are determined by using
        the "radius" as each value, resulting in a square.

        """
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius, TARGET_SAFE_COLOR)

    def hit(self):
        """
        If the target is hit,
        the target is no longer "alive" and will be removed
        Subtract 10 points, using the return

        """
        self.alive = False
        return -10
