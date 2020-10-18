def select():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, buttonFont

    dark_red = (175, 0, 0)
    red = (255, 0, 0)

    blue = (0, 0, 128)
    green = (0, 255, 0)
    dark_green = (0, 200, 0)


    rectW = 250
    rectH = 175

    gui.fill((0, 0, 0))
    spacebg()

    back = buttonFont.render("Back", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/6 <= mouse[0] <= width/6+rectW and height/6 <= mouse[1] <= height/6+rectH:
                print("Clicked")
            if width/2 <= mouse[0] <= width/2+rectW and height/6<= mouse[1] <= height/6+rectH:
                print("Clicked")
            if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
                main.screen = 0


    if width/6 <= mouse[0] <= width/6+rectW and height/6 <= mouse[1] <= height/6+rectH: 
        pygame.draw.rect(gui, red,[width/6, height/6, rectW, rectH]) 
        pygame.draw.rect(gui, dark_red,[width/2, height/6, rectW, rectH]) 
    elif width/2 <= mouse[0] <= width/2+rectW and height/6<= mouse[1] <= height/6+rectH:
        pygame.draw.rect(gui, dark_red, [width/6, height/6, rectW, rectH])
        pygame.draw.rect(gui, red,[width/2, height/6, rectW, rectH])
    else: 
        pygame.draw.rect(gui, dark_red, [width/6, height/6, rectW, rectH])
        pygame.draw.rect(gui, dark_red,[width/2, height/6, rectW, rectH])  

    #back button in bottom-left of screen
    if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
        pygame.draw.rect(gui, green, [10, 10, 70, 40])
    else:
        pygame.draw.rect(gui, dark_green, [10, 10, 70, 40])
    
    #back button for both setup.py and instructions.py
    gui.blit(back, (25, 15))