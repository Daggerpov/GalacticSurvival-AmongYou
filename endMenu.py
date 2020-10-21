def end():
    import main
    from main import gui, width, height, titleFont, buttonFont, mouse, pygame, posText, spacebg

    green = (0, 255, 0)
    red = (255, 0, 0)
    dark_red= (200, 0, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()

    #renders text for button
    menuButton = buttonFont.render("Return to Main Menu", True, blue)

    #Allows events/actions from mouse/keyboard
    for event in pygame.event.get(): 
        #The close window function
        if event.type == pygame.QUIT:
           quit()
        #checks if mouse clicks on the button
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-150 <= mouse[0] <= width/2+150 and height/4*3 <= mouse[1] <= height/4*3+40:
                main.screen = 0
                main.lose = False 
                main.game_end = False
                main.username = ''
                main.short_tasks = 1
                main.long_tasks = 0
                main.index = 1
                main.fails = 0
                
    
    #if lost then it randomizes between the 5 different loss messages and renders the text
    #otherwise, it'll just render the default win message
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

    #displays text
    gui.blit(endTitle, posText(endTitle, width//2, 75))

    #lights up button when hovering over
    if width/2-150 <= mouse[0] <= width/2+150 and height/4*3 <= mouse[1] <= height/4*3+40: 
        pygame.draw.rect(gui, red,[width/2-150, height/4*3, 300, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_red, [width/2-150, height/4*3, 300, 40]) 

    #displays button
    gui.blit(menuButton, (width/2-100, height/4*3+5))
