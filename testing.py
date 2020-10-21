'''
This file was meant for testing purposes before 
implementing the code into the actual game. This was used for our guidance 
and how to adjust each command to our liking in our game.
'''

import pygame
import sys, os
pygame.init() #Initializes the PyGame module

GUI = pygame.display.set_mode((500, 500)) #Makes Window
pygame.display.set_caption("Testing") #Title of Window

def reSizeRotate(image, width, height, angle):
    new_image = pygame.transform.rotate(pygame.transform.scale(image, (width, height)), angle)
    return new_image

clock = pygame.time.Clock()
timer = 10  # Decrease this to count down.
dt = 0  # Delta time (time since last tick).

#resources = pygame.font.get_fonts()
green = (0, 255, 0)
count = 0

x = 0
y = 0
angle = 270

rectx = 300
recty = 300

#When inserting PATH for new fonts, add 'r' infront to convert form string to raw string
font = pygame.font.Font('freesansbold.ttf', 69) #Font for text
posText = (0, 0) 
running = "True"

def drawStyleRect(screen):
    pygame.draw.rect(screen, (0,0,255), (rectx,recty,75,150), 0)
    for i in range(4):
        pygame.draw.rect(screen, (255,0,0), (rectx-i,recty-i,80,155), 3)

while running:
    pygame.time.delay(75) 
    for event in pygame.event.get(): #Allows events/actions from mouse/keyboard
        if event.type == pygame.QUIT: #The close window function
            running = False
        #if event.type == pygame.MOUSEBUTTONDOWN: #Testing Mouse-Clicked
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 50
                angle = 90
            if event.key == pygame.K_RIGHT:
                x += 50
                angle = 270
            if event.key == pygame.K_UP:
                y -= 50
                angle = 0
            if event.key == pygame.K_DOWN:
                y += 50
                angle = 180

    

    GUI.fill((0, 0, 0))   

    dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.
    txt = font.render(str(round(timer)), True, green)
    GUI.blit(txt, (500//2, 0))

    timer -= dt
    if timer <= 0:
        timer = 10

    #pygame.draw.rect(GUI, green,[x, y, 20, 20])
    image = reSizeRotate(pygame.image.load("./images/rocket.png"), 100, 80, angle)
    GUI.blit(image, (x, y))

    drawStyleRect(GUI)
    pygame.display.update() #Updates the screen
    

pygame.quit()
quit()