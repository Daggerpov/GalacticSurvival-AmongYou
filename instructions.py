def instruct():
    from main import pygame, gui, width, height, mouse, spacebg

    #colours


    gui.fill((0, 0, 0))
    spacebg()

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()

    