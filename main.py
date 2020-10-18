import pygame
import sys
import random

from startMenu import start
from endMenu import end
from setup import select
from instructions import instruct

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
textFont = pygame.font.Font(r'./in-your-face-joffrey/In your face, joffrey!.ttf', 28)

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

def back():
    blue = (0, 0, 128)
    green = (0, 255, 0)
    dark_green = (0, 200, 0)
    
    back = buttonFont.render("Back", True, blue)
    
    #back button in bottom-left of screen
    if width+35 <= mouse[0] <= width+105 and height+30 <= mouse[1] <= height+70:
        pygame.draw.rect(gui, green, [width, height, 70, 40])
    else:
        pygame.draw.rect(gui, dark_green, [width, height, 70, 40])
    
    #back button for both setup.py and instructions.py
    gui.blit(back, (width, height))

while running:
    pygame.time.delay(50) 

    mouse = pygame.mouse.get_pos()

    if screen == 0:
        start()

    elif screen == 1:
        select()
    
    elif screen == 2:
        instruct()

    else:
        end()
    
    pygame.display.update() #Updates the screen


pygame.quit()
quit() 