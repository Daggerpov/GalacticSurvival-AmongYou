def instruct():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, textFont, posText, buttonFont

    #colours
    dark_green = (0, 200, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()
    
    back = buttonFont.render("Back", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
                main.screen = 0

    text1 = textFont.render('Once you click the "Start Game" button in the main menu, you\'ll be', True, dark_green)
    text2 = textFont.render('given a choice of how many short/long tasks you would like you do.', True, dark_green)
    text3 = textFont.render('Each task will have a short explanation before it to tell you what', True, dark_green)
    text4 = textFont.render('the significance behind doing the task is (game lore) and what ', True, dark_green)
    text5 = textFont.render('the goal is in terms of completion. Based on the amount of each, ', True, dark_green)
    text6 = textFont.render('there will be a corresponding number of "retries" available to you', True, dark_green)
    text7 = textFont.render('throughout the game. Each time you run out of time or fail doing a', True, dark_green)
    text8 = textFont.render('task, the retry bar goes down 1. The game is won by completing all', True, dark_green)
    text9 = textFont.render('tasks and lost by running out of retries. Good luck!', True, dark_green)

    gui.blit(text1, posText(text1, width//2, height//2-200))
    gui.blit(text2, posText(text2, width//2, height//2-160))
    gui.blit(text3, posText(text3, width//2, height//2-120))
    gui.blit(text4, posText(text4, width//2, height//2-80))
    gui.blit(text5, posText(text5, width//2, height//2-40))
    gui.blit(text6, posText(text6, width//2, height//2))
    gui.blit(text7, posText(text7, width//2, height//2+40))
    gui.blit(text8, posText(text8, width//2, height//2+80))
    gui.blit(text9, posText(text9, width//2, height//2+120))

    #back button in bottom-left of screen
    if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
        pygame.draw.rect(gui, green, [10, 10, 70, 40])
    else:
        pygame.draw.rect(gui, dark_green, [10, 10, 70, 40])
    
    #back button for both setup.py and instructions.py
    gui.blit(back, (25, 15))