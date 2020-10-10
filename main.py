import pygame
import sys
import random
from startMenu import start, spacebg

pygame.init()

#Resolution dimensions
resx = 1366
resy = 768

gui = pygame.display.set_mode((resx, resy)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True

font = pygame.font.Font(r'C:\Users\Sanjeev\Documents\GitHub\ICS3U-firstGame\venv\Lib\site-packages\pygame\In your face, joffrey!.ttf',32)

stars = []

for i in range(200):
    starx = random.randrange(0, resx)
    stary = random.randrange(0, resy)
    stars.append([starx, stary])


while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #The close window function
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                running = False
    
    gui.fill((0, 0, 0))

    spacebg()
    start()
    
    pygame.display.update() #Updates the screen
pygame.quit()