import pygame
import math

from constants import *


SPEED = 100

x = 800
y = 600

def draw(screen, delta_time):
    """
    Draws the Woodhouse logo and makes it move away from the cursor at a constant speed
    """

    # in case you don't know, you can access outside variables in Python like this
    global x, y

    # update coordinates
    dist_x = pygame.mouse.get_pos()[0] - x
    dist_y = pygame.mouse.get_pos()[1] - y

    ratio = 100 / math.sqrt(dist_x**2 + dist_y**2)

    x -= dist_x * ratio * delta_time
    y -= dist_y * ratio * delta_time

    # ensure it doesn't leave screen
    if x < 0:
        x = 0
    elif x > SCREEN_WIDTH - 100:
        x = SCREEN_WIDTH - 100
    if y < 0:
        y = 0
    elif y > SCREEN_HEIGHT - 100:
        y = SCREEN_HEIGHT - 100

    # draw logo
    pygame.draw.rect(screen, "#8b8e93", (x, y, 100, 100))
    pygame.draw.polygon(screen, "#203878", [
        (x + 15, y - 15),
        (x + 30, y + 80),
        (x + 60, y + 50),
        (x + 75, y + 80),
        (x + 140, y + 5),
        (x + 75, y + 50),
        (x + 70, y + 15),
        (x + 40, y + 50)
    ])
