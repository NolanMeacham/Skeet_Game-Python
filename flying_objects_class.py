"""
CS241 - Flying Objects Class for Skeet
Written by Nolan Meacham

This class is used as a base for all flying objects in the skeet game. It is an abstract class, using the ABC
inheritance. The advance function here is used for each of the targets. The draw method is declared abstract and
is implemented in each of the specific objects instead of being implemented here.

"""

# Import statements
import arcade
from abc import ABC
from abc import abstractmethod
from point_class import Point
from velocity_class import Velocity


class FlyingObjects(ABC):
    """
    Flying Objects will include bullets, targets, and clouds.
        Center is set to Point, which is an x and y (x, y)
        Velocity is a dx and dy, which will be the amount of pixels and object moves each frame refresh.
        Radius is initialized to 0.0 but will be changed with each object
        Alive is used as a boolean. If the object is off the screen, the boolean becomes false, and the object should
            be removed, which is done by checking the alive boolean.
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True

    def advance(self):
        """
        Advances all of the flying objects (targets and bullets) by adding the value of the objects velocity to it's
            current position

        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def draw(self):
        """
        Abstract method, no implementation here.
        """
        pass

    def is_off_screen(self, screen_width, screen_height):
        """
        If the center of the object is less than zero in the x or y, it would be  off the screen and needs to be
            removed. The alive boolean is set to false and the method returns true, saying the object IS off screen.

        If the object's horizontal movement, (center.x), is greater than the screen width or
        If the vertical, (center.y), is greater than the screen height,
            the object is off screen. Alive boolean is set to false and method returns true, saying the object IS off
            screen.

        """
        if self.center.x < 0 or self.center.y < 0:
            self.alive = False
            return True
        if self.center.x > screen_width or self.center.y > screen_height:
            self.alive = False
            return True



