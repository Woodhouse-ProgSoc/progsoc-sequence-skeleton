import pygame
import math

from constants import *


SPEED = 100

x = 800
y = 600

def draw(screen, delta_time):
    """
    Draws the Woodhouse logo and makes it move away from the cursor at a constant speed.

    I made this as an example that you can use for reference on the basics. You're welcome to
    ask me how to do other things in Pygame too, or you can just Google it.
    """

    # in case you don't know, you can access outside variables in Python like this
    global x, y

    # update coordinates using some neat maths
    dist_x = pygame.mouse.get_pos()[0] - x
    dist_y = pygame.mouse.get_pos()[1] - y

    ratio = 100 / math.sqrt(dist_x**2 + dist_y**2)

    x_speed = dist_x * ratio
    y_speed = dist_y * ratio

    x -= x_speed * delta_time  # multiply the speed by `delta_time` to get the amount it should move by in just one frame
    y -= y_speed * delta_time

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


def handle_event(event):
    """
    Handling events example
    """

    if event.type == pygame.KEYDOWN:  # a key was pressed down
        if event.key == pygame.K_SPACE:  # check what key it was (type pygame.K to see a list of options)
            print("Space was pressed!")

    elif event.type == pygame.KEYUP:  # a key was released
        if event.key == pygame.K_a:
            print("The A key was pressed!")

    elif event.type == pygame.MOUSEBUTTONDOWN:  # the user clicked the mouse
        print(f"Click at {pygame.mouse.get_pos()}")
