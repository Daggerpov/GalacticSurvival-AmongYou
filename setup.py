def select():
    from main import pygame, gui, width, height, mouse, spacebg, back, screen

    dark_red = (175, 0, 0)
    red = (255, 0, 0)

    rectW = 250
    rectH = 175

    gui.fill((0, 0, 0))
    spacebg()
    
    back()

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/6 <= mouse[0] <= width/6+rectW and height/6 <= mouse[1] <= height/6+rectH:
                print("Clicked")
            if width/2 <= mouse[0] <= width/2+rectW and height/6<= mouse[1] <= height/6+rectH:
                print("Clicked")
            if width+35 <= mouse[0] <= width+105 and height+30 <= mouse[1] <= height+70:
                    screen = 0


    if width/6 <= mouse[0] <= width/6+rectW and height/6 <= mouse[1] <= height/6+rectH: 
        pygame.draw.rect(gui, red,[width/6, height/6, rectW, rectH]) 
        pygame.draw.rect(gui, dark_red,[width/2, height/6, rectW, rectH]) 

    elif width/2 <= mouse[0] <= width/2+rectW and height/6<= mouse[1] <= height/6+rectH:
        pygame.draw.rect(gui, dark_red, [width/6, height/6, rectW, rectH])
        pygame.draw.rect(gui, red,[width/2, height/6, rectW, rectH])
        

    else: 
        pygame.draw.rect(gui, dark_red, [width/6, height/6, rectW, rectH])
        pygame.draw.rect(gui, dark_red,[width/2, height/6, rectW, rectH])  