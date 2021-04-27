"""
CS241 - Bird Target for Skeet
Written by Nolan Meacham

The bird is a "Flying Object" and inherits the data from Target class, which gets data from the
Flying Objects class.

The bird is similar to the standard target. It is two arc outlines drawn to resemble a bird and takes one hit to remove
and adds 2 points when destroyed. It will always start from the left side of the screen, with a random velocity in the
x and y direction. The spawn area for the y value is randomly selected between the top half of the screen.

"""

import random
from globals import *
from target_class import Target


class Bird(Target):
    """
    Bird
    Inherits data from Target class using super()
    Redefines variables for x and y
    Although the bird does not need a radius to be drawn, it is used in the game class for check_collisions
    Define the velocity, as a random number between the ranges listed below

    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.uniform((SCREEN_HEIGHT / 2), SCREEN_HEIGHT)
        self.radius = STD_TARGET_RADIUS
        self.velocity.dx = random.uniform(1, 4)
        self.velocity.dy = random.uniform(-3, 1)

    def draw(self):
        """
        Draws each bird, using an image of a duck.png file and arcade's texture function

        """
        img = "duck.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1

        x = self.center.x
        y = self.center.y
        angle = 0

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
        """
        arcade.draw_arc_outline(self.center.x, self.center.y, 20, 20, arcade.color.BLACK, 0, 90)
        arcade.draw_arc_outline(self.center.x + 40, self.center.y, 20, 20, arcade.color.BLACK, 90, 180)
        """

    def hit(self):
        """
        This method is used simply to add 2 points to the users score using the return
         and set the alive boolean to false.

        """
        self.alive = False
        return 2
