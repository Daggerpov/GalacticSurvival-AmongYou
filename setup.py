def select():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, buttonFont, taskFont, posText

    plus = pygame.transform.scale(pygame.image.load("./images/Plus.png"), (100, 80))
    minus = pygame.transform.scale(pygame.image.load("./images/Minus.png"), (100, 80))

    

    blue = (0, 0, 128)
    green = (0, 255, 0)
    dark_green = (0, 200, 0)

    dark_red = (175, 0, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    dark_yellow = (215, 215, 0)

    increase_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_sound_digital_short_generic_could_be_collect_item_001_56968.wav")
    decrease_task_sound = pygame.mixer.Sound("./audio/zapsplat_multimedia_game_tone_marimba_high_pitched_generic_tone_003_56830.wav")
    error_task_sound = pygame.mixer.Sound("./audio/Computer Error Alert-SoundBible.com-783113881.wav")


    gui.fill((0, 0, 0))
    spacebg()

    back = buttonFont.render("Back", True, blue)

    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
                main.screen = 0
            
            if width-200 <= mouse[0] <= width-100 and height//4-40 <= mouse[1] <= height//4+40:
                if main.short_tasks == 0:
                    main.short_tasks += 1
                    pygame.mixer.Sound.play(increase_task_sound)
                else:
                    pygame.mixer.Sound.play(error_task_sound)
            
            if 100 <= mouse[0] <= 200 and height//4-40 <= mouse[1] <= height//4+40:
                if main.short_tasks == 1:
                    main.short_tasks -= 1
                    pygame.mixer.Sound.play(decrease_task_sound)
                else:
                    pygame.mixer.Sound.play(error_task_sound)

            if width-200 <= mouse[0] <= width-100 and height//1.25-40 <= mouse[1] <= height//1.25+40:
                if main.long_tasks == 0:
                    main.long_tasks += 1
                    pygame.mixer.Sound.play(increase_task_sound)
                else:
                    pygame.mixer.Sound.play(error_task_sound)

            if 100 <= mouse[0] <= 200 and height//1.25-40 <= mouse[1] <= height//1.25+40:
                if main.long_tasks == 1:
                    main.long_tasks -= 1
                    pygame.mixer.Sound.play(decrease_task_sound)
                else:
                    pygame.mixer.Sound.play(error_task_sound)

    '''
    if width-200 <= mouse[0] <= width-100 and height//4-40 <= mouse[1] <= height//4+40: 
        pygame.draw.polygon(gui, yellow, [(width-200, height//4-40), (width-100, height//4), (width-200, height//4+40)])
        pygame.draw.polygon(gui, dark_yellow, [(200, height//4-40), (100, height//4), (200, height//4+40)])

    elif 100 <= mouse[0] <= 200 and height//4-40 <= mouse[1] <= height//4+40:
       pygame.draw.polygon(gui, dark_yellow, [(width-200, height//4-40), (width-100, height//4), (width-200, height//4+40)])
       pygame.draw.polygon(gui, yellow, [(200, height//4-40), (100, height//4), (200, height//4+40)]) 

    else: 
        pygame.draw.polygon(gui, dark_yellow, [(width-200, height//4-40), (width-100, height//4), (width-200, height//4+40)])
        pygame.draw.polygon(gui, dark_yellow, [(200, height//4-40), (100, height//4), (200, height//4+40)])
    '''

    #back button in bottom-left of screen
    if 10 <= mouse[0] <= 80 and 10 <= mouse[1] <= 50:
        pygame.draw.rect(gui, green, [10, 10, 70, 40])
    else:
        pygame.draw.rect(gui, dark_green, [10, 10, 70, 40])
    
    #back button for both setup.py and instructions.py
    gui.blit(back, (25, 15))

    pygame.draw.polygon(gui, yellow, [(width-200, height//4-40), (width-100, height//4), (width-200, height//4+40)])
    pygame.draw.polygon(gui, yellow, [(200, height//4-40), (100, height//4), (200, height//4+40)])
    pygame.draw.polygon(gui, yellow, [(width-200, height//1.25-40), (width-100, height//1.25), (width-200, height//1.25+40)])
    pygame.draw.polygon(gui, yellow, [(200, height//1.25-40), (100, height//1.25), (200, height//1.25+40)])

    gui.blit(plus, (width//2-150, height//2-40))
    gui.blit(minus, (100, height//2-40))
    gui.blit(plus, (width-150, height//2-40))
    gui.blit(minus, (width//2+100, height//2-40))

    drawBorder(gui, width-200, height//4-40)
    drawBorder(gui, 100, height//4-40)
    drawBorder(gui, width-200, height//1.25-40)
    drawBorder(gui, 100, height//1.25-40)

    shortTasks = taskFont.render('Short Tasks = ' + str(main.short_tasks), True, (0, 255, 0)) #Initializing text
    longTasks = taskFont.render('Long Tasks = ' + str(main.long_tasks), True, (0, 255, 0)) #Initializing text
    gui.blit(shortTasks, posText(shortTasks, width//1.25, height//2)) #Printing text on screen, requires text and position
    gui.blit(longTasks, posText(longTasks, (width//4, height//2)) #Printing text on screen, requires text and position

def drawBorder(screen, bordx, bordy):
    from main import pygame
    for i in range(4):
        pygame.draw.rect(screen, (0, 255, 0), (bordx-i ,bordy-i , 105, 85), 1)
