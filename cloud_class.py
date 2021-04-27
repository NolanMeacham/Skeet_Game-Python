"""
CS241 - Cloud class for Skeet
Written by Nolan Meacham

This class is designed to draw clouds on the screen.
"""

import arcade
from globals import *
from flying_objects_class import FlyingObjects


class Cloud(FlyingObjects):
    """
    Clouds are "flying objects" and inherit data from the FlyingObjects class. I reinitialized the member data
    using the global declarations and random numbers for the center. This is so that each time a cloud object is
    created it will have a different position, so none of the clouds should start in the same spot.
    """
    def __init__(self):
        super().__init__()
        self.center.x = random.randint(1, SCREEN_WIDTH)
        self.center.y = random.randint((SCREEN_HEIGHT * 0.75), SCREEN_HEIGHT)
        self.radius = CLOUD_RADIUS
        self.color = CLOUD_COLOR
        self.velocity.dx = CLOUD_DX
        self.velocity.dy = CLOUD_DY

    def draw(self):
        """
        Clouds are drawn using 4 filled in circles, each with a center position varied from the original position
        so that the 4 circles create an image that looks like a cloud.

        """
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)
        arcade.draw_circle_filled((self.center.x - 30), (self.center.y - 12), self.radius, self.color)
        arcade.draw_circle_filled((self.center.x + 20), (self.center.y - 15), self.radius, self.color)
        arcade.draw_circle_filled((self.center.x - 10), (self.center.y - 20), self.radius, self.color)
