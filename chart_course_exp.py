def chart_course_exp():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, instructFont, posText, buttonFont

    #colours
    dark_green = (0, 200, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()

    proceedButton = buttonFont.render("Proceed", True, blue)
    
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width//2-50 <= mouse[0] <= width//2+70 and height//1.25-20 <= mouse[1] <= height//1.25+20:
                main.screen = 3.5
    
    text1 = instructFont.render('Chart the course of our ship to make sure we don\'t get lost!', True, dark_green)
    text2 = instructFont.render('Win: Successfully go through all the directions from start to end', True, dark_green)
    text3 = instructFont.render('Lose Retry: By moving to the wrong direction', True, dark_green)
    
    gui.blit(text1, posText(text1, width//2, height//2-100))
    gui.blit(text2, posText(text2, width//2, height//2-50))
    gui.blit(text3, posText(text3, width//2, height//2))

    if width//2-50 <= mouse[0] <= width//2+70 and height//1.25-20 <= mouse[1] <= height//1.25+20:
        pygame.draw.rect(gui, green, [width//2-50, height//1.25-20, 120, 40])
    else:
        pygame.draw.rect(gui, dark_green, [width//2-50, height//1.25-20, 120, 40])

    #proceed button
    gui.blit(proceedButton, posText(proceedButton, width//2+10, height//1.25))