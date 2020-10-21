def end():
    import main
    from main import gui, width, height, titleFont, buttonFont, mouse, pygame, posText, spacebg, lose

    import random

    green = (0, 255, 0)
    red = (255, 0, 0)
    dark_red= (200, 0, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()

    menuButton = buttonFont.render("Return to Main Menu", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                main.screen = 0
                main.username = ''
                main.short_tasks = 1
                main.long_tasks = 0
                main.index = 1
                main.lose = False 

                
    if width/2-60 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui, red,[width/2, height/2, 200, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_red, [width/2, height/2, 140, 40])
    

    if lose == True:
        which_message = random.randint(0, 5)

        messages = [
            f"{main.username}, you've doomed us all!", \
            "Oh no, the ship has been destroyed!", \
            f"{main.username}, what have you done?!", \
            "You've failed to save the ship!", \
            "You're worse than Daggerpov!" \
            ]
        endTitle = titleFont.render(messages[which_message], True, green)
    else:
        endTitle = titleFont.render("You've saved the ship!", True, green)

    gui.blit(endTitle , posText(endTitle, width//2, 75))
    gui.blit(menuButton , (width/2+40, height/2+5))
