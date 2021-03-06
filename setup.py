def select():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, buttonFont, taskFont, posText, instructFont, titleFont, retries

    plus = pygame.transform.scale(pygame.image.load("./images/Plus.png"), (100, 80))
    minus = pygame.transform.scale(pygame.image.load("./images/Minus.png"), (100, 80))

    #Colors
    blue = (0, 0, 128)
    green = (0, 255, 0)
    dark_green = (0, 200, 0)

    gui.fill((0, 0, 0))
    spacebg()

    back = buttonFont.render("Back", True, blue)
    start = buttonFont.render("Start Game", True, blue)

    textSurface = instructFont.render(main.username, True, blue)
    textPrompt = titleFont.render("Enter your username: ", True, green)

    #Allows events/actions from mouse/keyboard
    for event in pygame.event.get(): 
        #Close-Window
        if event.type == pygame.QUIT:
           quit()
        #Mouse-Clicked commands
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
                main.screen = 0
            
            if width//2-150 <= mouse[0] <= width//2-50 and height//2-90 <= mouse[1] <= height//2-10:
                if main.short_tasks == 0:
                    main.short_tasks += 1
                    pygame.mixer.Sound.play(main.increase_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
            
            if 100 <= mouse[0] <= 200 and height//2-90 <= mouse[1] <= height//2-10:
                if main.short_tasks == 1 and main.long_tasks == 1:
                    main.short_tasks -= 1
                    pygame.mixer.Sound.play(main.decrease_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)

            if width-150 <= mouse[0] <= width-50 and height//2-90 <= mouse[1] <= height//2-10:
                if main.long_tasks == 0:
                    main.long_tasks += 1
                    pygame.mixer.Sound.play(main.increase_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)

            if width//2+100 <= mouse[0] <= width//2+200 and height//2-90 <= mouse[1] <= height//2-10:
                if main.long_tasks == 1 and main.short_tasks == 1:
                    main.long_tasks -= 1
                    pygame.mixer.Sound.play(main.decrease_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
            
            if width//2+250 <= mouse[0] <= width//2+350 and height//2+55 <= mouse[1] <= height//2+135:
                if main.index < 3:
                    main.index += 1
                    pygame.mixer.Sound.play(main.increase_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)

            if width//2-325 <= mouse[0] <= width//2-225 and height//2+55 <= mouse[1] <= height//2+135:
                if main.index > 0:
                    main.index -= 1
                    pygame.mixer.Sound.play(main.decrease_task_sound)
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
            
            if width//2-50 <= mouse[0] <= width//2+70 and height//1.25 <= mouse[1] <= height//1.25+40:
                if main.username != '':
                    if main.short_tasks == 1:
                        main.screen = 3
                    elif main.long_tasks == 1:
                        main.screen = 4
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                main.username = main.username[:-1]
            else:
                main.username += event.unicode        

    #back button in top-left of screen
    if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
        pygame.draw.rect(gui, green, [10, 10, 70, 40])
    else:
        pygame.draw.rect(gui, dark_green, [10, 10, 70, 40])
    
    #back button for both setup.py and instructions.py
    gui.blit(back, (25, 15))

    #start button near lower-middle of screen
    if width//2-50 <= mouse[0] <= width//2+70 and height//1.25 <= mouse[1] <= height//1.25+40:
        pygame.draw.rect(gui, green, [width//2-50, height//1.25, 120, 40])
    else:
        pygame.draw.rect(gui, dark_green, [width//2-50, height//1.25, 120, 40])

    #Drawing start button
    gui.blit(start, posText(start, width//2+10, height//1.25+20))

    #Drawing the pluses/minuses for increments/decrements of tasks/difficulty
    gui.blit(plus, (width//2-150, height//2-90))
    gui.blit(minus, (100, height//2-90))
    gui.blit(plus, (width-150, height//2-90))
    gui.blit(minus, (width//2+100, height//2-90))
    gui.blit(plus, (width//2+250, height//2+55))
    gui.blit(minus, (width//2-325, height//2+55))

    #Drawing the names of the tasks/difficulty
    shortTasks = taskFont.render('Short Tasks = ' + str(main.short_tasks), True, (0, 255, 0)) #Initializing text
    longTasks = taskFont.render('Long Tasks = ' + str(main.long_tasks), True, (0, 255, 0)) #Initializing text
    difficultySlider = taskFont.render('Difficulty = ' + str(main.difficulty[main.index]), True, (0, 255, 0))
    gui.blit(shortTasks, posText(shortTasks, width//4+25, height//2-50)) #Printing text on screen, requires text and position
    gui.blit(longTasks, posText(longTasks, width//1.25-25, height//2-50)) #Printing text on screen, requires text and position
    gui.blit(difficultySlider, posText(difficultySlider, width//2, height//2+100))

    #drawing rect for main.username text input box
    pygame.draw.rect(gui, green, [main.userRectx, main.userRecty, textSurface.get_width() + 10, 50])
    
    #main.username text input box
    gui.blit(textSurface, (main.userRectx + 5, main.userRecty))

    gui.blit(textPrompt, posText(textPrompt, width//2+20, 75))