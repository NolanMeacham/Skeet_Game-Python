"""
CS241 - Strong Target for Skeet
Written by Nolan Meacham

The standard target is a "Flying Object" and inherits the data from Target class, which gets data from the
Flying Objects class.

The strong target is an outlined circle with a number inside it which represents the amount of "lives" or "armor" it
has left. The first two hits will award 1 point, the final/third hit will award five points. It follows the same
spawn pattern as the other targets.
"""

import random
from globals import *
from target_class import Target


class StrongTarget(Target):
    """
    Strong Target
    Inherit data from Target class using super()
    Redefine variables for x and y
    Define the radius using the global declaration from the globals file
    Define the velocity, as a random number between the ranges listed below.
    Define the starting lives for each target to 3

    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_HEIGHT)
        self.radius = STR_TARGET_RADIUS
        self.velocity.dx = random.uniform(1, 5)
        self.velocity.dy = random.uniform(-3, 3)
        self.lives = 3

    def draw(self):
        """
        Draws each strong target.
        The text_x and text_y are used to draw the number in the center of the target as it moves.
        The self.lives variable is used so that each time the target is hit, the number will change accordingly

        """
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, STR_TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, STR_TARGET_COLOR, font_size=20)

    def hit(self):
        """
        This method is called by the skeet game if it recognizes that the user has shot the target (the objects
            have "collided")
        If the target has more than 1 life left,
            the target is still "alive"
            reduce the amount of lives by 1 when it is hit
            award 1 point, using the return
        If the target only has 1 life remaining,
            the target is no longer alive
            award 5 points for destroying a strong target, using the return

        """
        if self.lives > 1:
            self.lives -= 1
            return 1

        elif self.lives == 1:
            self.alive = False
            return 5
