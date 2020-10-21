def simon_says():
    import main 
    from main import pygame, gui, width, height, mouse, buttonFont, posText, spacebg, instructFont, colour_names, Pcol0, Pcol1, Pcol2, Pcol3, Pcol4, Pcol5, Pcol6, Pcol7, Pcol8, pattern

    image_size = 154

    gui.fill((0, 0, 0))
    spacebg()
    green = (0, 255, 0)
    

    order = instructFont.render(f"This is the pattern order: {colour_names[pattern[0]]}, {colour_names[pattern[1]]}, {colour_names[pattern[2]]}, {colour_names[pattern[3]]}, {colour_names[pattern[4]]}.", True, green)


    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 774 <= mouse[0] <= 774+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol0 = main.ai[0]
                pygame.draw.rect(gui, Pcol0, [774, 154, image_size, image_size])
                if pattern[main.clicks] == Pcol0:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1 
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                
    
            if 929 <= mouse[0] <= 929+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol1 = main.ai[1]
                pygame.draw.rect(gui, Pcol1, [929, 154, image_size, image_size]) 
                if pattern[main.clicks] == Pcol1:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1 
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                
                    
            if 1084 <= mouse[0] <= 1084+image_size and 154 <= mouse[1] <= 154+image_size:
                Pcol2 = main.ai[2]
                pygame.draw.rect(gui, Pcol2, [1084, 154, image_size, image_size])
                if pattern[main.clicks] == Pcol2:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1 
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                

            if 774 <= mouse[0] <= 774+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol3 = main.ai[3]
                pygame.draw.rect(gui, Pcol3, [774, 309, image_size, image_size]) 
                if pattern[main.clicks] == Pcol3:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1 
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                

            if 929 <= mouse[0] <= 929+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol4 = main.ai[4]
                pygame.draw.rect(gui, Pcol4, [929, 309, image_size, image_size]) 
                if pattern[main.clicks] == Pcol4:
                    pygame.mixer.Sound.play(main.increase_task_sound) 
                    main.clicks += 1
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                

            if 1084 <= mouse[0] <= 1084+image_size and 309 <= mouse[1] <= 309+image_size:
                Pcol5 = main.ai[5]
                pygame.draw.rect(gui, Pcol5, [1084, 309, image_size, image_size])
                if pattern[main.clicks] == Pcol5:
                    pygame.mixer.Sound.play(main.increase_task_sound) 
                    main.clicks += 1
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                

            if 774 <= mouse[0] <= 774+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol6 = main.ai[6]
                pygame.draw.rect(gui, Pcol6, [774, 464, image_size, image_size]) 
                if pattern[main.clicks] == Pcol6:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1 
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                
                
            if 929 <= mouse[0] <= 929+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol7 = main.ai[7]
                pygame.draw.rect(gui, Pcol7, [929, 464, image_size, image_size]) 
                if pattern[main.clicks] == Pcol7:
                    pygame.mixer.Sound.play(main.increase_task_sound)
                    main.clicks += 1
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                
                
                
            if 1084 <= mouse[0] <= 1084+image_size and 464 <= mouse[1] <= 464+image_size:
                Pcol8 = main.ai[8]
                pygame.draw.rect(gui, Pcol8, [1084, 464, image_size, image_size])
                if pattern[main.clicks] == Pcol8:
                    pygame.mixer.Sound.play(main.increase_task_sound) 
                    main.clicks += 1
                else:
                    pygame.mixer.Sound.play(main.error_task_sound)
                    main.fails -= 1
                    main.screen = 4
                
                

    if main.clicks == 5:
        main.game_end = True
        main.screen = 5

    pygame.draw.rect(gui, Pcol0, [774, 154, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol1, [929, 154, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol2, [1084, 154, image_size, image_size])
    pygame.draw.rect(gui, Pcol3, [774, 309, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol4, [929, 309, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol5, [1084, 309, image_size, image_size])
    pygame.draw.rect(gui, Pcol6, [774, 464, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol7, [929, 464, image_size, image_size]) 
    pygame.draw.rect(gui, Pcol8, [1084, 464, image_size, image_size])

    pygame.draw.rect(gui, main.ai[0], [154, 154, image_size, image_size])
    pygame.draw.rect(gui, main.ai[1], [309, 154, image_size, image_size]) 
    pygame.draw.rect(gui, main.ai[2], [464, 154, image_size, image_size])
    pygame.draw.rect(gui, main.ai[3], [154, 309, image_size, image_size]) 
    pygame.draw.rect(gui, main.ai[4], [309, 309, image_size, image_size]) 
    pygame.draw.rect(gui, main.ai[5], [464, 309, image_size, image_size])
    pygame.draw.rect(gui, main.ai[6], [154, 464, image_size, image_size]) 
    pygame.draw.rect(gui, main.ai[7], [309, 464, image_size, image_size]) 
    pygame.draw.rect(gui, main.ai[8], [464, 464, image_size, image_size])
    
    gui.blit(order, posText(order, width//2+20, 75))