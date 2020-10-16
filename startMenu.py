def start():
    import main
    from main import pygame, gui, width, height, buttonFont, mouse, titleFont, posText, spacebg
    

    green = (0, 255, 0)
    dark_green= (0, 200, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()
    startTitle = titleFont.render("Galactic Survival: Among You", True, green)
    startbutton = buttonFont.render("Start", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                print("Clicked")
                main.screen = 1
                
                
            

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui, green,[width/2, height/2, 140, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_green, [width/2, height/2, 140, 40]) 
    

    gui.blit(startTitle , posText(startTitle, width//2, 75))
    # superimposing the text onto our button 
    gui.blit(startbutton , (width/2+30, height/2+5))


