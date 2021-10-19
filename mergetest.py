import pygame


def draw(screen, x, y):
    pygame.draw.rect(screen, (100, 0, 200), (x, y, 100, 100))
