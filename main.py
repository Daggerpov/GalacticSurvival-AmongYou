import pygame
import sys
import random
from startMenu import start
from endMenu import end
from task_selection import select

pygame.init()

#Resolution dimensions
resx = 1366
resy = 768

gui = pygame.display.set_mode((resx, resy)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True

titleFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 100)
buttonFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 32)

def posText(text, x, y):
    titleRect = text.get_rect()
    titleRect.center = (x, y)
    return titleRect

green = (0, 255, 0)

stars = []

screen = 0

for i in range(125):
    starx = random.randrange(0, resx)
    stary = random.randrange(0, resy)
    stars.append([starx, stary])

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



while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    start()

    if screen == 1:
        select()
    #end()
    pygame.display.update() #Updates the screen


pygame.quit()
quit() 