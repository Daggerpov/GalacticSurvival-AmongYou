def run():
    from main import gui, width, height, font, mouse, pygame

    green = (0, 255, 0)
    dark_green= (0, 200, 0)
    blue = (0, 0, 128)

    startbutton = font.render("Start", True, blue)
    
    gui.fill((0, 0, 0))

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui, green,[width/2, height/2, 140, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_green, [width/2, height/2, 140, 40]) 
    
    # superimposing the text onto our button 
    gui.blit(startbutton , (width/2+30, height/2+5))