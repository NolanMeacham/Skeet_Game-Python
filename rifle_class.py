"""
CS241 - Skeet - Week 06 - Rifle Class
Written by Nolan Meacham

"""

import arcade
from globals import *
from point_class import Point


class Rifle:
    """
    The rifle is a rectangle that tracks the mouse and is drawn at (0, 0) 
    which is the bottom left corner of the screen.
    This is where the bullets will come from.
    """
    def __init__(self):
        self.center = Point()

        self.angle = 45

    def draw(self):
        """
        Draw the rifle, as a rectangle in the bottom left corner of the screen

        I made changes to this function so that the rifle will appear to look like a rifle barrel
        hand-guard/stock.

        """
        # Draw the rifle barrel
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_BARREL_WIDTH, RIFLE_BARREL_HEIGHT,
                                     RIFLE_BARREL_COLOR, -self.angle)
        # Draw the rifle hand guard/stock
        arcade.draw_rectangle_filled(self.center.x+4, self.center.y-2, RIFLE_STOCK_WIDTH, RIFLE_STOCK_HEIGHT,
                                     RIFLE_STOCK_COLOR, -self.angle)



