def simon_says():
    import main 
    from main import pygame, gui, width, height, mouse, buttonFont, posText, spacebg
    import random

    silver = (192, 192, 192)
    blue = (50, 50, 255)
    image_size = 154
    
    Pcol0 = silver
    Pcol1 = silver
    Pcol2 = silver
    Pcol3 = silver
    Pcol4 = silver
    Pcol5 = silver
    Pcol6 = silver
    Pcol7 = silver
    Pcol8 = silver

    P = [Pcol0, Pcol1, Pcol2, Pcol3, Pcol4, Pcol5, Pcol6, Pcol7, Pcol8]

    col0 = silver
    col1 = silver
    col2 = silver
    col3 = silver
    col4 = silver
    col5 = silver
    col6 = silver
    col7 = silver
    col8 = silver

    ai = [col0, col1, col2, col3, col4, col5, col6, col7, col8]

    gui.fill((0, 0, 0))
    spacebg()

    pattern = []
    for i in range(5):
        pattern.append(random.randint(0, 8))
        for j in pattern:
            P[j] = blue
            #pygame.time.delay(500)
            P[j] = silver
        

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 774 <= mouse[0] <= 774+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol0 = blue
                pygame.time.delay(500)
            if 929 <= mouse[0] <= 929+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol1 = blue
                pygame.time.delay(500)
            if 1084 <= mouse[0] <= 1084+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol2 = blue
                pygame.time.delay(500)
            if 774 <= mouse[0] <= 774+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol3 = blue
                pygame.time.delay(500)
            if 929 <= mouse[0] <= 929+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol4 = blue
                pygame.time.delay(500)
            if 1084 <= mouse[0] <= 1084+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol5 = blue
                pygame.time.delay(500)
            if 774 <= mouse[0] <= 774+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol6 = blue
                pygame.time.delay(500)
            if 929 <= mouse[0] <= 929+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol7 = blue
                pygame.time.delay(500)
            if 1084 <= mouse[0] <= 1084+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol8 = blue
                pygame.time.delay(500)
    
    pygame.draw.rect(gui, Pcol0, [774, 154, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol1, [929, 154, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol2, [1084, 154, image_size, image_size])
    pygame.draw.rect(gui, Pcol3, [774, 309, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol4, [929, 309, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol5, [1084, 309, image_size, image_size])
    pygame.draw.rect(gui, Pcol6, [774, 464, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol7, [929, 464, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol8, [1084, 464, image_size, image_size])

    pygame.draw.rect(gui, col0, [154, 154, image_size, image_size])
    pygame.draw.rect(gui, col1, [309, 154, image_size, image_size]) 
    pygame.draw.rect(gui, col2, [464, 154, image_size, image_size])
    pygame.draw.rect(gui, col3, [154, 309, image_size, image_size]) 
    pygame.draw.rect(gui, col4, [309, 309, image_size, image_size]) 
    pygame.draw.rect(gui, col5, [464, 309, image_size, image_size])
    pygame.draw.rect(gui, col6, [154, 464, image_size, image_size]) 
    pygame.draw.rect(gui, col7, [309, 464, image_size, image_size]) 
    pygame.draw.rect(gui, col8, [464, 464, image_size, image_size])
    