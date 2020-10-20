def chart_course():
    import main 
    from main import pygame, gui, width, height, mouse, buttonFont, taskFont, posText, timer

    gui.fill((115, 194, 251)) #Light Blue

    main.angle = 180

    timer(15)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main.rocketx -= 20
                main.angle = 90
            if event.key == pygame.K_RIGHT:
                main.rocketx += 20
                main.angle = 270
            if event.key == pygame.K_UP:
                main.rockety -= 20
                main.angle = 0
            if event.key == pygame.K_DOWN:
                main.rockety += 20
                main.angle = 180

    rocket = reSizeRotate(pygame.image.load("./images/rocket.png"), 100, 80, main.angle)

    gui.blit(rocket, (main.rocketx, main.rockety))

def reSizeRotate(image, width, height, angle):
    new_image = pygame.transform.rotate(pygame.transform.scale(image, (width, height)), angle)
    return new_image

'''def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    import numpy
    import math
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)
'''