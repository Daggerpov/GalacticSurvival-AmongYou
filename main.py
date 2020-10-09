import pygame
import sys
from startMenu import run

pygame.init()

gui = pygame.display.set_mode((1366, 768)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True

font = pygame.font.Font('freesansbold.ttf',32)

while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                running = False
    
    run()
    
    pygame.display.update() #Updates the screen
pygame.quit()