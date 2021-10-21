import pygame


def draw(screen, x, y):
    """
    An example drawing made by Sergi.

    Duplicate this file, replace my name with yours, and change the code to draw something more interesting!

    Try to keep the whole drawing roughly 100 by 100 pixels
    """

    pygame.draw.rect(screen, (150, 0, 200), (x+20, y + 90, 70, 80))
    # this function draws a rectangle
    # (0, 0, 200) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (0, 50, 100, 50) are the dimensions of the rectangle in the form (top-left x coordinate, top-left y coordinate, width, height)
    # Remember that y increases as you go down the screen

    pygame.draw.polygon(screen, (59, 205, 0), [(x + 20, y + 20), (x + 24, y + 90), (x + 175, y + 90)])
    # this function draws any polygon (in this case, a triangle)
    # (200, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # [(x + 0, y + 50), (x + 50, y + 0), (x + 100, y + 50)] is a list of all the vertices of the polygon, i.e.:
    # [(x coord, y coord), (x coord, y coord), (x coord, y coord)]

    pygame.draw.circle(screen, (29, 25, 20), (x + 60, y + 60), 50)
    # this function draws a circle
    # (0, 100, 100) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (x + 25, x + 25) are the x and y coordinates of its center
    # 10 is the radius

    pygame.draw.ellipse(screen, (200, 20, 0), (x + 25, y + 25, 20, 60))
    pygame.draw.ellipse(screen, (200, 20, 0), (x + 50, y + 25, 20, 60))
    # this function draws an ellipse
    # (200, 200, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # imagine the smallest rectangle that would touch all the sides of the ellipse, then:
    # (x + 25, x + 25, 30, 70) is (top left of the rectangle's x coordinate, y coordinate, width, height)

    pygame.draw.line(screen, (250, 250, 250), (x + 10, y + 10), (x + 100, y +100 ))
    # this function draws a line
    # (0, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (x + 0, y + 0) are the coordinates of one end
    # (x + 100, y + 100) are the coordinates of the other end

    pygame.draw.lines(screen, (0, 0, 0), False, [(x + 10, y + 10), (x + 20, y + 10), (x + 20, y + 20)])
    # this function draws many connected lines at once
    # (0, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # False is whether it should draw a line between the first point and the last point
    # [(x + 10, y + 10), (x + 20, y + 10), (x + 20, y + 20)] is a list of all the points
