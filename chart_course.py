def chart_course():
    import main
    import random 
    from main import pygame, gui, width, height, mouse, buttonFont, posText, fails

    #this is done instead of the menus' space background, so that it's individual to this one task
    light_blue = (115, 194, 251)
    gui.fill(light_blue) 
    
    #makes the grid's individual squares, 8x4 based on our display resolution (1366x768p)
    grid(width, height, 170.75, 192)

    rocketPos = [main.rocketx, main.rockety]
    
    #allows events/actions from mouse/keyboard
    for event in pygame.event.get():
        #if you hit command/control + Q or just quit out of the program by clicking
        if event.type == pygame.QUIT:
           quit()
        #key presses
        if event.type == pygame.KEYDOWN:
            #arrow keys
            if event.key == pygame.K_LEFT:
                main.rocketx -= 170.75
                main.angle = 270
            if event.key == pygame.K_RIGHT:
                main.rocketx += 170.75
                main.angle = 270
            if event.key == pygame.K_UP:
                main.rockety -= 192
                main.angle = 0
            if event.key == pygame.K_DOWN:
                main.rockety += 192
                main.angle = 180

    #this determines whether the rocket has reached the end goal position
    if rocketPos == main.endPos:
        #this will redirect to the long task when done if there is one, otherwise it'll head to the end screen
        if main.long_tasks == 1:
            main.screen = 4
        else:
            main.game_end = True
            main.screen = 5

    #this adds a fail to be subtracted by the retry attempts when rocket crashes into wall
    if rocketPos[1] > 576 or rocketPos[1] < 0 or rocketPos[0] > 1195.25 or rocketPos[0] < 0:
        main.fails += 1
        main.screen = 3

    #this generates the sprite image to be the rocket
    rocket = reSizeRotate(pygame.image.load("./images/rocket.png"), 171, 192, main.angle)

    #draw the end goal square as red
    pygame.draw.rect(gui, (255, 0, 0), [main.endPos[0], main.endPos[1], 170.75, 192])

    #displays rocket at current coordinates
    gui.blit(rocket, (main.rocketx, main.rockety))

#rotates the rocket when hitting other arrow keys
def reSizeRotate(image, width, height, angle):
    from main import pygame
    new_image = pygame.transform.rotate(pygame.transform.scale(image, (width, height)), angle)
    return new_image

#generates the whole grid to be displayed
def grid(width, height, image_width, image_height):
    import main
    from main import pygame

    for x in range(int(width//image_width)):
        for y in range(int(height//image_height)):
            rect = pygame.Rect(x*image_width, y*image_height, image_width, image_height)
            pygame.draw.rect(main.gui, (255, 255, 255), rect, 2)
