def instruct():
    from main import pygame, gui, width, height, mouse, spacebg, textFont

    #colours
    black = (0, 0, 0)
    dark_green = (0, 200, 0)

    gui.fill((0, 0, 0))
    spacebg()

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()

    text = textFont.render('''
    Once you click the "Start Game" button in the main menu, you'll be
    given a choice of how many short/long tasks you would like you do. 
    Each task will have a short explanation before it to tell you what
    the significance behind doing the task is (game lore) and what 
    the goal is in terms of completion. Based on the amount of each, 
    there will be a corresponding number of "retries" available to you
    throughout the game. Each time you run out of time or fail doing a
    task, the retry bar goes down 1. The game is won by completing all 
    tasks and lost by running out of retries. Good luck!''', True, black, dark_green)

    text_rect = text.get_rect()

    text_rect.center = (width // 2, height // 2)