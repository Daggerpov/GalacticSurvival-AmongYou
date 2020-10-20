import pygame
import sys
import random
import time

from startMenu import start
from endMenu import end
from setup import select
from instructions import instruct

from chart_course_exp import chart_course_exp
from simon_says_exp import simon_says_exp
from chart_course import chart_course 
from simon_says import simon_says


pygame.init()

#Resolution dimensions
resx = 1366
resy = 768

gui = pygame.display.set_mode((resx, resy)) 
width = gui.get_width()
height = gui.get_height()

pygame.display.set_caption("Galactic Survival: Among You") #Title of Window
running = True

titleFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 100)
buttonFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 32)
taskFont = pygame.font.Font(r'./fonts/In your face, joffrey!.ttf', 50)
instructFont = pygame.font.Font(r'./fonts/NegaraSerif-HairlineItalic.otf', 32)

def posText(text, x, y):
    titleRect = text.get_rect()
    titleRect.center = (x, y)
    return titleRect

green = (0, 255, 0)

stars = []

username = ''
userRect = pygame.Rect(width//2-125, height//4-20, 200, 40)

screen = 0

short_tasks = 1
long_tasks = 0

difficulty = ['easy', 'normal', 'hard', 'extreme']
index = 1

angle = 0
rocketx = 80
rockety = 80

for i in range(60):
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

def timer(length):
    dark_red = (200, 0, 0)
    for i in range(1, length+1):
        time = instructFont.render(str(i), True, dark_red)
        gui.blit(time, posText(time, width-10, 10))
        #time.sleep(1)

while running:
    pygame.time.delay(10) 

    mouse = pygame.mouse.get_pos()

    if screen == 0:
        start()

    elif screen == 1:
        select()
    
    elif screen == 2:
        instruct()

    elif screen == 3:
        if short_tasks == 1:
            chart_course_exp()
        elif long_tasks == 1:
            simon_says_exp()

    elif screen == 3.5:
        if short_tasks == 1:
            chart_course()
        elif long_tasks == 1:
            simon_says()

    elif screen == 4 and long_tasks == 1:
        simon_says_exp()
    
    elif screen == 4.5:
        simon_says()

    else:
        end()
    
    pygame.display.update() #Updates the screen

pygame.quit()
quit() 