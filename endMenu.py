def end():
    import main
    from main import gui, width, height, titleFont, buttonFont, mouse, pygame, posText, spacebg


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
            if width/2-150 <= mouse[0] <= width/2+150 and height/4*3 <= mouse[1] <= height/4*3+40:
                main.screen = 0
                main.lose = False 
                main.game_end = False
                main.username = ''
                main.short_tasks = 1
                main.long_tasks = 0
                main.index = 1
                main.fails = 0
                
    

    if main.lose == True:
        messages = [
            f"{main.username}, you've doomed us all!", \
            "Oh no, the ship has been destroyed!", \
            f"{main.username}, what have you done?!", \
            "You've failed to save the ship!", \
            "You're worse than Daggerpov!" \
            ]
        endTitle = titleFont.render(messages[main.which_message], True, green)
    else:
        endTitle = titleFont.render("You've saved the ship!", True, green)

    gui.blit(endTitle, posText(endTitle, width//2, 75))


    if width/2-150 <= mouse[0] <= width/2+150 and height/4*3 <= mouse[1] <= height/4*3+40: 
        pygame.draw.rect(gui, red,[width/2-150, height/4*3, 300, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_red, [width/2-150, height/4*3, 300, 40]) 

    gui.blit(menuButton, (width/2-100, height/4*3+5))
