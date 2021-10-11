import pygame

from sergi import drawing_sergi


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


def update(screen):
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit program
            exit()

    # draw onto screen
    screen.fill((255, 255, 255))

    drawing_sergi(screen, 100, 100)

    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        update(screen)


if __name__ == "__main__":
    main()
