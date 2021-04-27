"""
CS241 - Skeet Game Class
Implemented/Revised by Nolan Meacham

File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""

# Import statements
import arcade
import math
import random
from rifle_class import Rifle
from bullet_class import Bullet
from slug_class import Slug
from std_target import StandardTarget
from str_target import StrongTarget
from safe_target import SafeTarget
from bird_class import Bird
from cloud_class import Cloud
from globals import *


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # Initialize the list of targets to an empty list
        self.targets = []

        # List of clouds
        self.clouds = []

        # I set the background color to sky blue to set up a background for the game
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Initialize this to zero to create variables. These will be changed in
        # the on_mouse_motion by setting them equal to the x and y of the mouse
        # which will be used in other functions
        self.mouse_x = 0.0
        self.mouse_y = 0.0

        # Determine the number of clouds to add to the list. This is initialized here
        # so that the game will start with a random number of clouds each time it's played
        self.num_clouds = random.randint(0, 5)
        # A loop to add Cloud objects to the list of clouds.
        for i in range(self.num_clouds):
            self.clouds.append(Cloud())

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # Draw the grass
        arcade.draw_rectangle_filled(GRASS_X, GRASS_Y, GRASS_WIDTH, GRASS_HEIGHT, GRASS_COLOR)
        # Draw the sun
        arcade.draw_circle_filled(SUN_X, SUN_Y, SUN_RADIUS, SUN_COLOR)

        # Draw a tree
        arcade.draw_rectangle_filled(660, 215, 8, 40, arcade.color.OTTER_BROWN)
        arcade.draw_triangle_filled(650, 210, 670, 210, 660, 272, arcade.color.BANGLADESH_GREEN)
        arcade.draw_triangle_filled(650, 225, 670, 225, 660, 278, arcade.color.BANGLADESH_GREEN)

        # Draw the text for firing options
        shoot_options = "-Click to fire one bullet.\n"\
                        "-Press 'SPACE' to shoot volley of 5 bullets.\n"\
                        "-Press 'S' to fire a big slug shot"
        arcade.draw_text(shoot_options, 150, 45, arcade.color.BLACK)

        # draw the rifle
        self.rifle.draw()

        # A loop used to draw each bullet
        for bullet in self.bullets:
            bullet.draw()

        # A loop used to draw each target
        for target in self.targets:
            target.draw()

        # A loop to draw clouds
        for cloud in self.clouds:
            cloud.draw()

        # Call the draw_score method
        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = (SCREEN_HEIGHT - 20)
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.BLACK)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        # A loop used to advance each cloud
        for cloud in self.clouds:
            cloud.advance()

        # A loop used to advance each bullet
        for bullet in self.bullets:
            bullet.advance()

        # A loop used to advance each target in the list.
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.

        """

        # I used a random number variable (rand_target) in order to randomize the target created each time this function
        # is called.
        stand = StandardTarget()
        strong = StrongTarget()
        safe = SafeTarget()
        bird = Bird()

        rand_target = random.randint(1, 4)
        if rand_target == 1:
            self.targets.append(stand)
        elif rand_target == 2:
            self.targets.append(strong)
        elif rand_target == 3:
            self.targets.append(safe)
        elif rand_target == 4:
            self.targets.append(bird)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                            abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets, targets, or clouds have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

        for cloud in self.clouds:
            if cloud.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.clouds.remove(cloud)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """
        Uses the mouse position to determine the position of the rifle.
        Also set a mouse_x and mouse_y variable to the x and y position of the mouse so that we can
        use this position for other methods.
        """
        self.mouse_x = x
        self.mouse_y = y
        
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)
        

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """
        Uses the mouses position to set (x, y) to call get_angle function
        Fires a bullet
        """
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def on_key_press(self, key, key_modifiers):
        """
        Use the space bar to fire a shotgun spray of 5 bullets or
        use 's' to fire a single, large and slow slug bullet
        """
        # If the user presses the space bar
        if key == arcade.key.SPACE:

            # Use the mouse (x, y) to set the angle for the shotgun fire
            angle = self._get_angle_degrees(self.mouse_x, self.mouse_y)

            # Create 5 bullet objects
            bullet1 = Bullet()
            bullet2 = Bullet()
            bullet3 = Bullet()
            bullet4 = Bullet()
            bullet5 = Bullet()

            # Fire each bullet, each with a slightly different angle to create the shotgun spray
            bullet1.fire(angle - 2)
            bullet2.fire(angle - 1)
            bullet3.fire(angle)
            bullet4.fire(angle + 1)
            bullet5.fire(angle + 2)

            # Add each bullet to the list of bullets
            self.bullets.append(bullet1)
            self.bullets.append(bullet2)
            self.bullets.append(bullet3)
            self.bullets.append(bullet4)
            self.bullets.append(bullet5)

        # If the user presses the 's' key
        if key == arcade.key.S:
            # Use the mouse pointer x and y to set the angle
            angle = self._get_angle_degrees(self.mouse_x, self.mouse_y)
            # Create a slug object
            slug1 = Slug()

            # Call the fire command for the slug
            slug1.fire(angle)

            # Add the slug to the list of bullets
            self.bullets.append(slug1)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
