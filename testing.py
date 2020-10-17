import pygame
import os
pygame.init() #Initializes the PyGame module

GUI = pygame.display.set_mode((500, 500)) #Makes Window
pygame.display.set_caption("Testing") #Title of Window

#resources = pygame.font.get_fonts()
#title = pygame.image.load(os.path.join('data', 'GalacticSurvivalTitle.png'))
green = (0, 255, 0)
count = 0

x = 500/6
y = 500/6

#When inserting PATH for new fonts, add 'r' infront to convert form string to raw string
font = pygame.font.Font('freesansbold.ttf', 69) #Font for text
posText = (0, 0) 
running = "True"

while running:
    pygame.time.delay(75) 
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT: #The close window function
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN: #Testing Mouse-Clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_DOWN:
                y += 10
        
    GUI.fill((0, 0, 0))   

    pygame.draw.rect(GUI, green,[x, y, 20, 20])
        
    pygame.display.update() #Updates the screen
pygame.quit()
quit()