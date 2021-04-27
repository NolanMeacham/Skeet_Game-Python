"""
CS241 - Skeet - Week 06 - Globals file
Written by Nolan Meacham

These global declarations are used for setting up the game window and each object characteristics.

"""

import arcade
import random
# These are Global constants to use throughout the game

# Screen Dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# SUN and GRASS are used to draw the background
# SUN
SUN_X = (SCREEN_WIDTH - 30)
SUN_Y = (SCREEN_HEIGHT - 30)
SUN_RADIUS = 50
SUN_COLOR = arcade.color.GOLDEN_YELLOW
# GRASS
GRASS_X = SCREEN_WIDTH / 2
GRASS_Y = (SCREEN_HEIGHT / 2) - 200
GRASS_WIDTH = SCREEN_WIDTH
GRASS_HEIGHT = (SCREEN_HEIGHT / 3)
GRASS_COLOR = arcade.color.APPLE_GREEN

# CLOUDS
CLOUD_X = random.randint(1, SCREEN_WIDTH)
CLOUD_Y = random.randint((SCREEN_HEIGHT * 0.75), SCREEN_HEIGHT)
CLOUD_DX = -.07
CLOUD_DY = 0
CLOUD_RADIUS = 25
CLOUD_COLOR = arcade.color.ANTIQUE_WHITE

# Rifle attributes
# Rifle Barrel
RIFLE_BARREL_WIDTH = 150
RIFLE_BARREL_HEIGHT = 20
RIFLE_BARREL_COLOR = arcade.color.GRAY_BLUE
# Rifle Stock
RIFLE_STOCK_WIDTH = 80
RIFLE_STOCK_HEIGHT = 15
RIFLE_STOCK_COLOR = arcade.color.GOLDEN_BROWN

# Bullet attributes
BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.SMOKY_BLACK
BULLET_SPEED = 10

# Standard target
STD_TARGET_RADIUS = 15
STD_TARGET_COLOR = arcade.color.CARROT_ORANGE

# Strong target
STR_TARGET_RADIUS = 15
STR_TARGET_COLOR = arcade.color.RED_ORANGE

# Safe target
TARGET_SAFE_COLOR = arcade.color.BLUE_SAPPHIRE
TARGET_SAFE_RADIUS = 15
