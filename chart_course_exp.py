def chart_course_exp():
    import main
    from main import pygame, gui, width, height, mouse, spacebg, instructFont, posText, buttonFont, titleFont, retries, username

    #colours
    dark_green = (0, 200, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    #required for all space backgrounds to be black, then have the snowfall type animation for stars
    gui.fill((0, 0, 0))
    spacebg()

    #rendering text for button with anti-aliasing that has blue text
    proceedButton = buttonFont.render("Proceed", True, blue)
    
    #rendering text for the retry amount by incorporating the retry variable
    retryAmount = titleFont.render(f"Retries: {retries}", True, green) 

    #allows events/actions from keyboard and mouse to be registered
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width//2-50 <= mouse[0] <= width//2+70 and height//1.25-20 <= mouse[1] <= height//1.25+20:
                main.screen = 3.5
    
    #renders all the text, anti-aliasing is ON (True) and it's dark green
    text1 = instructFont.render('Chart the course of our ship to make sure we don\'t get lost!', True, dark_green)
    text2 = instructFont.render('Win: Successfully go through all the directions from start to end', True, dark_green)
    text3 = instructFont.render('Lose Retry: By moving to the wrong direction', True, dark_green)
    text4 = instructFont.render(f'You have 10 seconds for this task, {username}', True, dark_green)

    #displays the text for explanation
    gui.blit(text1, posText(text1, width//2, height//2-100))
    gui.blit(text2, posText(text2, width//2, height//2-50))
    gui.blit(text3, posText(text3, width//2, height//2))
    gui.blit(text4, posText(text3, width//2, height//2+50))

    #lights up if hovering over proceed button
    if width//2-50 <= mouse[0] <= width//2+70 and height//1.25-20 <= mouse[1] <= height//1.25+20:
        pygame.draw.rect(gui, green, [width//2-50, height//1.25-20, 120, 40])
    else:
        pygame.draw.rect(gui, dark_green, [width//2-50, height//1.25-20, 120, 40])

    #proceed button
    gui.blit(proceedButton, posText(proceedButton, width//2+10, height//1.25))

    #retry text display
    gui.blit(retryAmount, posText(retryAmount, width//2, 75))