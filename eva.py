import pygame


def drawing_eva(screen, x, y):

    #pygame.draw.rect(screen, (255, 0, 0), (x, y + 50, 100, 50))
    # this function draws a rectangle
    # (0, 0, 200) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (0, 50, 100, 50) are the dimensions of the rectangle in the form (top-left x coordinate, top-left y coordinate, width, height)
    # Remember that y increases as you go down the screen

    pygame.draw.polygon(screen, ((240, 234, 217)), [(x + 0, y + 100), (x + 50, y + 100), (x + 50, y + 0)])
    pygame.draw.polygon(screen, ((240, 234, 217)), [(x + 105, y + 100), (x + 55, y + 100), (x + 55, y + 0)])
    pygame.draw.polygon(screen, (30, 198, 242), [(x + 0, y + 105), (x + 55, y + 200), (x + 115, y + 105), (x + 45, y + 105), (x + 15, y + 105) ])

    # this function draws any polygon (in this case, a triangle)
    # (200, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # [(x + 0, y + 50), (x + 50, y + 0), (x + 100, y + 50)] is a list of all the vertices of the polygon, i.e.:
    # [(x coord, y coord), (x coord, y coord), (x coord, y coord)]

   # pygame.draw.circle(screen, (0, 200, 200), (x + 25, y + 25), 20)
    # this function draws a circle
    # (0, 100, 100) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (x + 25, x + 25) are the x and y coordinates of its center
    # 10 is the radius

   # pygame.draw.ellipse(screen, (200, 200, 0), (x + 25, y + 25, 30, 70))
    # this function draws an ellipse
    # (200, 200, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # imagine the smallest rectangle that would touch all the sides of the ellipse, then:
    # (x + 25, x + 25, 30, 70) is (top left of the rectangle's x coordinate, y coordinate, width, height)

    #pygame.draw.line(screen, (0, 0, 0), (x + 0, y + 0), (x + 100, y + 100))
    # this function draws a line
    # (0, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # (x + 0, y + 0) are the coordinates of one end
    # (x + 100, y + 100) are the coordinates of the other end

    #pygame.draw.lines(screen, (0, 0, 0), False, [(x + 10, y + 10), (x + 20, y + 10), (x + 20, y + 20)])
    # this function draws many connected lines at once
    # (0, 0, 0) is the colour in RGB form. Google "colour picker", choose a colour and copy the RGB value
    # False is whether it should draw a line between the first point and the last point
    # [(x + 10, y + 10), (x + 20, y + 10), (x + 20, y + 20)] is a list of all the points
