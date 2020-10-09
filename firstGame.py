import pygame
import os
pygame.init() #Initializes the PyGame module

GUI = pygame.display.set_mode((500, 500)) #Makes Window
pygame.display.set_caption("Galactic Survival: Among You") #Title of Window

#resources = pygame.font.get_fonts()
title = pygame.image.load(os.path.join('data', 'GalacticSurvivalTitle.png'))
green = (0, 255, 0)
count = 0

#font = pygame.font.Font('', 32) #Font for text
posText = (0, 0) 
running = "True"

while running:
    pygame.time.delay(75) 
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        #if event.type == pygame.MOUSEBUTTONDOWN: #Testing Mouse-Clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Testing out left arrow key
                count-=1 
            elif event.key == pygame.K_RIGHT: #Testing out right arrow key
                count+=1 
        GUI.fill((0, 0, 0)) #The background of the display window
        text = font.render('Count = ' + str(count), True, green) #Initializing text
        GUI.blit(text, posText) #Printing text on screen, requires text and position
        if event.type == pygame.QUIT: #The close window function
            running = False
    pygame.display.update() #Updates the screen
pygame.quit()'''