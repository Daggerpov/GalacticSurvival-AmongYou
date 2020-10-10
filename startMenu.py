def start():
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

 

def spacebg():
    from main import resx, resy, running, gui, pygame, stars, starx , stary
    import random

    for i in range(len(stars)):
        # Draw the star
        pygame.draw.circle(gui, (255, 255, 255), stars[i], 2)
        # Move the star right one pixel
        stars[i][0] += 1
        # If the star has moved off the bottom of the screen
        if stars[i][0] > resx:
            # Reset it just above the top
            starx = random.randrange(-50, -10)
            stars[i][0] = starx
            # Give it a new y position
            stary = random.randrange(0, resy)
            stars[i][1] = stary

