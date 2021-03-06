import pygame
import time

from constants import *

import rowena
import sergi
import nick
import jessie
import mergetest
import sergi_interactive
import eva
import Mario
import Amina

delta_time = 0
"""
Approximate duration of current frame in seconds. Multiply by this to get smooth movement.
"""

def update(screen):
    global delta_time

    # handle events
    for event in pygame.event.get():
        sergi_interactive.handle_event(event)

        if event.type == pygame.QUIT:
            # quit program
            exit()

    # clear previous frame from screen
    screen.fill((255, 255, 255))

    rowena.draw(screen, 700, 300)
    jessie.draw(screen, 100, 100)
    mergetest.draw(screen, 300, 100)
    sergi_interactive.draw(screen, delta_time)
    eva.drawing_eva(screen, 150, 500)
    sergi.draw(screen, 300, 300)
    Mario.draw(screen, 500, 200)
    Amina.draw(screen, 500, 500)
    nick.draw(screen, 400, 400)

    # actually show the contents of `screen` on the monitor
    pygame.display.flip()



def main():
    global delta_time

    pygame.init()
    # this must be called before using Pygame

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    """
    The Pygame surface to draw on if you want to draw onto the screen.
    """

    while True:
        start_time = time.time()

        update(screen)

        delta_time = time.time() - start_time


if __name__ == "__main__":
    main()
