def end():
    from main import gui, width, height, titleFont, mouse, pygame
    

    green = (0, 255, 0)
    dark_green= (0, 200, 0)
    blue = (0, 0, 128)

    endTitle = titleFont.render("You're Worse Than Daggerpov!", True, green)
    titleRect = endTitle.get_rect()
    titleRect.center = (width//2, 75)
    
    # superimposing the text onto our button 
    gui.blit(endTitle , titleRect)