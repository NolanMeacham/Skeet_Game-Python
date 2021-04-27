"""
CS241 - Target Class for Skeet
Written by Nolan Meacham

The target class is an abstract class but also inherits data from the flying object class. It is used for the
four different types of targets:
1. Standard (std)
2. Strong (str)
3. Safe (safe)
4. Bird (bird)

"""

# Import statements
from abc import ABC
from abc import abstractmethod
from flying_objects_class import FlyingObjects


class Target(FlyingObjects, ABC):
    """
    Target Class
    Inherits data from flying objects using the super() command
    Abstract class (ABC)
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        """
        Abstract method, no implementation here.

        """
        pass

    @abstractmethod
    def hit(self):
        """
        Abstract method, no implementation here.

        """
        pass
