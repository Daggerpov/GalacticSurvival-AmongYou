def end():
    from main import gui, width, height, titleFont, buttonFont, mouse, pygame, posText, spacebg

    green = (0, 255, 0)
    red = (255, 0, 0)
    dark_red= (200, 0, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()


    endTitle = titleFont.render("You're Worse Than Daggerpov!", True, green)
    retrybutton = buttonFont.render("Retry", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                print("Clicked")

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui, red,[width/2, height/2, 140, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_red, [width/2, height/2, 140, 40])
    
    gui.blit(endTitle , posText(endTitle, width//2, 75))

    gui.blit(retrybutton , (width/2+30, height/2+5))