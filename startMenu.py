import pygame
import sys

pygame.init()

gui = pygame.display.set_mode((1000, 700)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True
green = (0, 255, 0)
dark_green= (0, 200, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf',32)
startbutton = font.render("Start", True, blue)

while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                running = False
    
    gui.fill((0,0,0))

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui,green,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(gui,dark_green,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    gui.blit(startbutton , (width/2+30,height/2+5))
    pygame.display.update() #Updates the screen
pygame.quit()