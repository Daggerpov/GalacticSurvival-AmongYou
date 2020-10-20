def simon_says():
    import main 
    from main import pygame, gui, width, height, mouse, buttonFont, posText, spacebg

    silver = (192, 192, 192)
    blue = (50, 50, 255)
    image_size = 154
    
    Pcol1 = silver
    Pcol2 = silver
    Pcol3 = silver
    Pcol4 = silver
    Pcol5 = silver
    Pcol6 = silver
    Pcol7 = silver
    Pcol8 = silver
    Pcol9 = silver    
    
    col1 = silver
    col2 = silver
    col3 = silver
    col4 = silver
    col5 = silver
    col6 = silver
    col7 = silver
    col8 = silver
    col9 = silver

    gui.fill((0, 0, 0))
    spacebg()

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 774 <= mouse[0] <= 774+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol1 = blue
            if 929 <= mouse[0] <= 929+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol2 = blue
            if 1084 <= mouse[0] <= 1084+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol3 = blue
            if 774 <= mouse[0] <= 774+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol4 = blue
            if 929 <= mouse[0] <= 929+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol5 = blue
            if 1084 <= mouse[0] <= 1084+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol6 = blue
            if 774 <= mouse[0] <= 774+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol7 = blue
            if 929 <= mouse[0] <= 929+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol8 = blue
            if 1084 <= mouse[0] <= 1084+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol9 = blue
    
    player_pad = [pygame.draw.rect(gui, Pcol1, [774, 154, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol2, [929, 154, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol3, [1084, 154, image_size, image_size]),
    pygame.draw.rect(gui, Pcol4, [774, 309, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol5, [929, 309, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol6, [1084, 309, image_size, image_size]),
    pygame.draw.rect(gui, Pcol7, [774, 464, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol8, [929, 464, image_size, image_size]), 
    pygame.draw.rect(gui, Pcol9, [1084, 464, image_size, image_size])]

    ai_pad = [pygame.draw.rect(gui, col1, [154, 154, image_size, image_size]), 
    pygame.draw.rect(gui, col2, [309, 154, image_size, image_size]), 
    pygame.draw.rect(gui, col3, [464, 154, image_size, image_size]),
    pygame.draw.rect(gui, col4, [154, 309, image_size, image_size]), 
    pygame.draw.rect(gui, col5, [309, 309, image_size, image_size]), 
    pygame.draw.rect(gui, col6, [464, 309, image_size, image_size]),
    pygame.draw.rect(gui, col7, [154, 464, image_size, image_size]), 
    pygame.draw.rect(gui, col8, [309, 464, image_size, image_size]), 
    pygame.draw.rect(gui, col9, [464, 464, image_size, image_size])]
    