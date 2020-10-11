def select():
    from main import pygame, gui, width, height, mouse

    dark_red = (175, 0, 0)
    red = (255, 0, 0)

    if width/4 <= mouse[0] <= width/4+250 and height/4 <= mouse[1] <= height/4+100: 
        pygame.draw.rect(gui, red,[width/4, height/4, 250, 100]) 
        
    else: 
        pygame.draw.rect(gui, dark_red, [width/4, height/4, 250, 100])  