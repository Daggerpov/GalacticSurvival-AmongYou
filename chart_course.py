def chart_course():
    import main
    import random 
    from main import pygame, gui, width, height, mouse, buttonFont, posText

    light_blue = (115, 194, 251)

    gui.fill(light_blue) 
    grid(width, height, 170.75, 192)

    rocketPos = [main.rocketx, main.rockety]
    
    '''for i in main.path:
        pygame.draw.rect(gui, (255, 0, 0), [main.path[i][0], main.path[i][1], 170.75, 192])'''

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                main.rocketx += 170.75
                main.angle = 270
            if event.key == pygame.K_UP:
                main.rockety -= 192
                main.angle = 0
            if event.key == pygame.K_DOWN:
                main.rockety += 192
                main.angle = 180

    if rocketPos == main.endPos:
        if main.long_tasks == 1:
            main.screen = 4
        else:
            main.screen = 10

    if rocketPos[1] > 576 or rocketPos[1] < 0:
        main.retries -= 1
        main.screen = 3

    rocket = reSizeRotate(pygame.image.load("./images/rocket.png"), 171, 192, main.angle)

    pygame.draw.rect(gui, (255, 0, 0), [main.endPos[0], main.endPos[1], 170.75, 192])

    gui.blit(rocket, (main.rocketx, main.rockety))

def reSizeRotate(image, width, height, angle):
    from main import pygame
    new_image = pygame.transform.rotate(pygame.transform.scale(image, (width, height)), angle)
    return new_image

def grid(width, height, image_width, image_height):
    import main
    from main import pygame

    for x in range(int(width//image_width)):
        for y in range(int(height//image_height)):
            rect = pygame.Rect(x*image_width, y*image_height, image_width, image_height)
            pygame.draw.rect(main.gui, (255, 255, 255), rect, 2)
